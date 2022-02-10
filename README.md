
# Flask Web API

Web application with one endpoint that takes a keyword in its URL string, uses it as an
input into the NYPL Digital Collections API, and returns the title and link of the books found using the specified keyword
in the API using the programming language Python and framework Flask along with the unit test for the same.



## Running the Web API

To run the Web API, run the following command

```bash
  python app.py
```



## Running Tests

To run tests, run the following command

```bash
  python test.py
```


## Sample outputs
```http
1. When url given as http://127.0.0.1:5000/?keyword=cats
{
    "data": [
        {
            "itemLink": "http://digitalcollections.nypl.org/items/b992a521-9c85-2498-e040-e00a18063ad7",
            "title": "Three cats watching fish in an aquarium"
        },
        {
            "itemLink": "http://digitalcollections.nypl.org/items/88b2c083-bb4c-1645-e040-e00a180605dc",
            "title": "[Maeghde Wapen [Maiden's Arms]"
        },
        {
            "itemLink": "http://digitalcollections.nypl.org/items/510d47d9-49f8-a3d9-e040-e00a18064a99",
            "title": "The boy who drew cats"
        }
    ]
}
```

```http
2. When url gievn as http://127.0.0.1:5000/?keyword=jhjkns
{
    "message": "Data not found using the given keyword: jhjkns"
}
```

```http
3. When url gievn as http://127.0.0.1:5000/
{
    "message": "Please provide a keyword or enter in url using the format: /?keyword=valid_keyword"
}
```

```http
4. When url gievn as http://127.0.0.1:5000/cats
{
    "message": "Please provide a keyword or enter in url using the format: /?keyword=valid_keyword"
}
```