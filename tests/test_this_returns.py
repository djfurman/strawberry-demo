from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport


def test_this_runs():
    transport = AIOHTTPTransport(url="http://127.0.0.1:5000/graphql")

    client = Client(transport=transport, fetch_schema_from_transport=True)

    query = gql(
        """
        query fetchBooks {
            books {
                title
                author
            }
        }
        """
    )

    result = client.execute(query)

    assert result.get("books") is not None
    assert len(result["books"]) == 1

    for book in result["books"]:
        assert book.get("title") is not None
        assert book.get("author") is not None
