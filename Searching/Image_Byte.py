def _get_image_bytes(received_input):
    """Converts the incoming input into raw bytes ready for upload."""
    if isinstance(received_input, bytes):
        return received_input
    elif isinstance(received_input, Image.Image):
        buf = io.BytesIO()
        received_input.convert("RGB").save(buf, format="JPEG")
        return buf.getvalue()
    elif isinstance(received_input, np.ndarray):
        img = Image.fromarray(received_input)
        buf = io.BytesIO()
        img.save(buf, format="JPEG")
        return buf.getvalue()
    elif isinstance(received_input, str):
        with open(received_input, "rb") as f:
            return f.read()
    else:
        raise ValueError(f"Unsupported input type: {type(received_input)}")

