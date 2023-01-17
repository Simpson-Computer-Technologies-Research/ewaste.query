
def wrap(title: str, description: str, url: str):
    return (
        f"""
        <div style="margin-right: 50vw; margin-left: 20px;">
            <a style="font-size: 20px;" href="{url}">
                {title}
            </a>
            <br>
            <mark style="color: green; background: none;">
                {url}
            </mark>
            <br>
            {description}
            <br><br>
        </div>
        """
    )
