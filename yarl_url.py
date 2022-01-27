# If you want to use Python to quickly build a URL using information such as scheme, host, port, path, query, fragment, etc, try yarl.
# yarl also makes it easy to replace one part with another, such as a query.
from yarl import URL

# create a URL
url = URL.build(
    scheme="https",
    host="github.com",
    path="/search",
    query={"p": 2, "q": "data science"},
)
print(url)

print(url.with_query("q=python"))

print(url.with_path("khuyentran1401/Data-science"))

