
{% markdown %}
# Report for {{ user.name }}

**Date:** {{ report.date }}

### Summary
{{ report.summary }}

## Details
{% for item in report["items"] %}
- {{ item }}
{% endfor %}

---

## Image
![Report Image]({{ image_url }})

*Generated automatically.*
{% endmarkdown %}