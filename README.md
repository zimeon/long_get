# long_get.py

Small python program to do a GET that will timeout because it says it has content which is then not sent. Created to simulate errors seen at arXiv that generated spurious 500 responses which should instead have been 400/408 or such.

## Example use

arXiv now handles such requests gracefully with an appropriate timeout:

``` bash
simeon@RottenApple long_get>./long_get.py http://arxiv.org/

Doing GET on http://arxiv.org/
> GET / HTTP/1.1
> Host: arxiv.org
> User-Agent: long_get
> Content-Length: 1000
> 

After 120s, got:
< HTTP/1.1 400 Bad Request
< Date: Thu, 22 Sep 2016 18:59:49 GMT
< Server: Apache
< Content-Length: 285
< Connection: close
< Content-Type: text/html; charset=iso-8859-1
< Set-Cookie: BIGipServer~SVCCENTER~arxiv-web.arxiv.org_http_pool=rd822o00000000000000000000ffff80540423o80; path=/; Httponly
< 
```

Google sits and hangs for longer than I am patient:

```
simeon@RottenApple long_get>./long_get.py http://google.com/

Doing GET on http://google.com/
> GET / HTTP/1.1
> Host: google.com
> User-Agent: long_get
> Content-Length: 1000
> 
^C
```
