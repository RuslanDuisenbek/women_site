menu = [{'title': 'About site', 'url_name': 'about'},
        {'title': 'Add statue', 'url_name': 'addpage'},
        {'title': 'Remote connection', 'url_name': 'contacts'}]


class DataMixin:
    paginate_by = 3
    title_page = None
    cat_selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected

    def get_mixin_data(self, content, **kwargs):
        content['cat_selected'] = None
        content.update(kwargs)
        return content
