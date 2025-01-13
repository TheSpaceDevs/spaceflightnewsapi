from django.contrib.admin.templatetags.admin_urls import admin_urlname
from django.db.models.query import QuerySet
from django.shortcuts import resolve_url
from django.utils.html import format_html
from django.utils.safestring import SafeString


def foreign_keys_to_html(foreign_model: django.db.models.Model, elements: QuerySet) -> SafeString:
    """Returns a string of admin hyperlinks to the foreign model objects."""
    text = ""
    if not elements:
        return "None"
    for element in elements:
        url = resolve_url(admin_urlname(foreign_model._meta, "change"), element.id)
        if hasattr(element, "name"):
            name = element.name
        else:
            name = "Object"
        text += f'<a href="{url}">{str(name)}</a>, '

    authors_list = [resolve_url(admin_urlname(foreign_model._meta, "change"), author.id) for author in elements]
    string = [authors_list[i:i+3] for i in range(0, len(authors_list), 3)]  # Group into lines of up to 3 authors
    split_string = "<br>".join([", ".join(line) for line in string])  # Format each line and join with <br>
    return format_html(split_string)
