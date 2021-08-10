from rest_framework.renderers import BaseRenderer


class PNGBinaryFileRenderer(BaseRenderer):
    media_type = 'image/png'
    Format = 'png'
    charset = 'utf-8'
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data
