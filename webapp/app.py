from flask import Flask, request, render_template_string, send_file
import pandas as pd
from io import BytesIO
from lvt_utils import model_split_rate_tax


def load_dataset(file_storage, url):
    """Load a CSV from an uploaded file or a URL."""
    if url:
        return pd.read_csv(url)
    if file_storage:
        return pd.read_csv(file_storage)
    raise ValueError("No data provided")

app = Flask(__name__)

UPLOAD_FORM = """
<!doctype html>
<title>LVTShift Web</title>
<h2>Load Parcel Data</h2>
<form method=post enctype=multipart/form-data>
  <p>Dataset URL (optional): <input type=text name=url size=60></p>
  <p>Or upload CSV: <input type=file name=file></p>
  Land value column: <input type=text name=land_value_col value="REALLANDVA" required><br>
  Improvement value column: <input type=text name=improvement_value_col value="REALIMPROV" required><br>
  Current revenue (number): <input type=text name=current_revenue required><br>
  Land/Improvement ratio: <input type=text name=ratio value="4"><br>
  Exemption column (optional): <input type=text name=exemption_col><br>
  Exemption flag column (optional): <input type=text name=exemption_flag_col><br>
  Percentage cap column (optional): <input type=text name=percentage_cap_col><br>
  <input type=submit value=Process>
</form>
"""

RESULT_TEMPLATE = """
<!doctype html>
<title>Results</title>
<h2>Split Rate Results</h2>
<p>Land millage: {{ land_millage:.2f }}</p>
<p>Improvement millage: {{ improvement_millage:.2f }}</p>
<p>New total revenue: {{ new_revenue:,.2f }}</p>
<p><a href="/download">Download full results CSV</a></p>
{{ table|safe }}
"""

result_buffer = BytesIO()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data_url = request.form.get('url')
        file = request.files.get('file')
        try:
            df = load_dataset(file, data_url)
        except Exception as e:
            return f"Failed to load dataset: {e}", 400
        land_col = request.form['land_value_col']
        improve_col = request.form['improvement_value_col']
        current_revenue = float(request.form['current_revenue'])
        ratio = float(request.form.get('ratio', 4))
        exemption_col = request.form.get('exemption_col') or None
        exemption_flag_col = request.form.get('exemption_flag_col') or None
        pct_cap_col = request.form.get('percentage_cap_col') or None

        land_mill, improve_mill, new_rev, result_df = model_split_rate_tax(
            df,
            land_value_col=land_col,
            improvement_value_col=improve_col,
            current_revenue=current_revenue,
            land_improvement_ratio=ratio,
            exemption_col=exemption_col,
            exemption_flag_col=exemption_flag_col,
            percentage_cap_col=pct_cap_col,
        )

        global result_buffer
        result_buffer = BytesIO()
        result_df.to_csv(result_buffer, index=False)
        result_buffer.seek(0)
        table_html = result_df.head().to_html()
        return render_template_string(
            RESULT_TEMPLATE,
            land_millage=land_mill,
            improvement_millage=improve_mill,
            new_revenue=new_rev,
            table=table_html,
        )
    return UPLOAD_FORM

@app.route('/download')
def download_results():
    global result_buffer
    if result_buffer.getbuffer().nbytes == 0:
        return "No results available", 404
    result_buffer.seek(0)
    return send_file(result_buffer, as_attachment=True, download_name='lvt_results.csv', mimetype='text/csv')

if __name__ == '__main__':
    app.run(debug=True)
