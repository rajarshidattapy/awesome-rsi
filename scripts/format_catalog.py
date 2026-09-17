"""Render researcher-maintained README entries."""


def entry(org, title, url, date, source, focus, quote, why, evidence):
    return (
        f"**[{org} — {title}]({url})**  \n"
        f"{date} · {source}  \n"
        f"Focus: {focus}\n\n"
        f"> {quote}\n\n"
        f"Why it matters: {why}  \n"
        f"Evidence: {evidence}\n"
    )


AUTH = "Author-reported results; independent replication not established."
AUTH_CODE = "Author-reported results with official code; independent replication not established."
CO = "Company-reported results; independent replication not established."
PROTO = "Evaluation protocol; does not itself demonstrate recursive self-improvement."
THEORY = "Formal or position argument; not an empirical demonstration of RSI."
SURVEY = "Secondary synthesis; not a primary experimental result."
IMPL = "Public implementation; repository activity is not independent scientific validation."
