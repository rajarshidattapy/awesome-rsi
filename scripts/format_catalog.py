"""Helpers for compact README paper entries."""


def paper(title, url, org, date, source, tags, abstract):
    tag_line = " ".join(f"`{t}`" for t in tags)
    return (
        f"### [{title}]({url}) — {org}\n"
        f"*{date} · {source}*\n\n"
        f"tags: {tag_line}\n\n"
        f"> **Abstract:** {abstract}\n"
    )
