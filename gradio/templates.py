from gradio import components


class Text(components.Textbox):
    """
    Sets: lines=1
    """

    is_template = True

    def __init__(self, **kwargs):
        super().__init__(lines=1, **kwargs)


class TextArea(components.Textbox):
    """
    Sets: lines=7
    """

    is_template = True

    def __init__(self, **kwargs):
        super().__init__(lines=7, **kwargs)


class Webcam(components.Image):
    """
    Sets: source="webcam"
    """

    is_template = True

    def __init__(self, **kwargs):
        super().__init__(source="webcam", **kwargs)


class Sketchpad(components.Image):
    """
    Sets: image_mode="L", source="canvas", shape=(28, 28), invert_colors=True
    """

    is_template = True

    def __init__(self, **kwargs):
        super().__init__(
            image_mode="L",
            source="canvas",
            shape=(28, 28),
            invert_colors=True,
            **kwargs
        )

class OnlineSketchpad(components.Image):

    is_template = True

    def __init__(self, **kwargs):
        super().__init__(
            image_mode="L",
            source="canvas",
            shape=(28, 28),
            invert_colors=True,
            type="json",
            **kwargs
        )
    def preprocess(self, x):
        import json
        x_obj = json.loads(x)

        x_obj['lines'][0]['points'][0]['x']
        x_list =  [[[int(point['x']), int(point['y'])] for point in line['points']]  for line in x_obj['lines']]
        return str(x_list)

    def postprocess(self, y):
        return y



class Pil(components.Image):
    """
    Sets: type="pil"
    """

    is_template = True

    def __init__(self, **kwargs):
        super().__init__(type="pil", **kwargs)


class PlayableVideo(components.Video):
    """
    Sets: format="mp4"
    """

    is_template = True

    def __init__(self, **kwargs):
        super().__init__(format="mp4", **kwargs)


class Microphone(components.Audio):
    """
    Sets: source="microphone"
    """

    is_template = True

    def __init__(self, **kwargs):
        super().__init__(source="microphone", **kwargs)


class Mic(components.Audio):
    """
    Sets: source="microphone"
    """

    is_template = True

    def __init__(self, **kwargs):
        super().__init__(source="microphone", **kwargs)


class Files(components.File):
    """
    Sets: file_count="multiple"
    """

    is_template = True

    def __init__(self, **kwargs):
        super().__init__(file_count="multiple", **kwargs)


class Numpy(components.Dataframe):
    """
    Sets: type="numpy"
    """

    is_template = True

    def __init__(self, **kwargs):
        super().__init__(type="numpy", **kwargs)


class Matrix(components.Dataframe):
    """
    Sets: type="array"
    """

    is_template = True

    def __init__(self, **kwargs):
        """
        Custom component
        @param kwargs:
        """
        super().__init__(type="array", **kwargs)


class List(components.Dataframe):
    """
    Sets: type="array"
    """

    is_template = True

    def __init__(self, **kwargs):
        """
        Custom component
        @param kwargs:
        """
        super().__init__(type="array", col_count=1, **kwargs)


class Highlight(components.HighlightedText):
    is_template = True

    def __init__(self, **kwargs):
        """
        Custom component
        @param kwargs:
        """
        super().__init__(**kwargs)
