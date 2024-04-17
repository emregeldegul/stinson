## Stinson

Finansal destek uygulaması, backend projesi. DRF kullanılarak geliştirilmiştir ve Docker ile dağıtılmıştır. Amaç, finansal destek almak isteyen e-ticaret uygulaması kullanıcıların başvuru yapabileceği bir uygulama sunmaktır. Bu bağlamda 2 endpoint mevcuttur.

1.  Application Endpoint
2.  Channel Endpoint

Application Endpoint, kullanıcıların başvuruyu gerçekleştirdikleri ilk adıma ait endpoint'tir. Burada ilk başvuru sonrası oluşacak token, ikinci başvuruda kullanılmalıdır.

Channel Endpoint, ilk başvuruda üretilen token ile beraber müşterinin trendyol, amazon gibi pazar yerleri -marketplace- bilgilerin içerir. İlk adımda verilen token olmadan işlem yapılamaz.

### Kurulum

Proje, talep edilirse sanal ortamda manuel kurulabileceği gibi talebe göre Docker servisi de kullanılabilir.

#### Manuel

```bash
~$ git clone https://github.com/emregeldegul/stinson.git && cd stinson
~$ virtualenv venv # kendi versiyon yönetim aracınızı kullanabilirsiniz.
~$ pip install -r requirements.txt
~$ python manage.py migrate
~$ python manage.py createsuperuser  # isteğe bağlı.
```

#### Docker

```bash
~$ git clone https://github.com/emregeldegul/stinson.git && cd stinson
~$ docker-compose run web python manage.py migrate
~$ docker-compose run web python manage.py createsuperuser  # isteğe bağlı
~$ docker-compose up
```

### Testler

Testleri çalıştırmak için Django'nın test komutu kullanılabilir.
```
~$ python manage.py test
```

### Kullanım

Proje 2 adet endpoint'e sahiptir.

<table><tbody><tr><td>Endpoint</td><td>Method</td><td>URL</td></tr><tr><td>Application</td><td>POST</td><td><a href="http://127.0.0.1:8000/api/merchant/application">http://127.0.0.1:8000/api/merchant/application</a></td></tr><tr><td>Channel</td><td>POST</td><td><a href="http://127.0.0.1:8000/api/merchant/channel">http://127.0.0.1:8000/api/merchant/channel</a></td></tr></tbody></table>

Örnek payloadlar aşağıda verilmiştir.

**Application:**

```json
{
    "first_name": "Osman",
    "last_name": "Şaşkınbakkal",
    "email": "osmansaskinbakkal147@hotmail.com",
    "phone_number": "+905111111111"
}
```

**Channel:**

```json
{
    "website_url": "https://emregeldegul.com.tr",
    "trendyol_url": "https://emregeldegul.com.tr",
    "amazon_url": "https://emregeldegul.com.tr",
    "token": "<TOKEN_FROM_THE_PREVIOUS_PHASE>"
}
```

### Katkı

Proje düzeni için pre-commit kullanılmaktadır. Katkı sağlamadan önce pre-commit scriptinin aktif olduğundan emin olun yada manuel kontrol sağlayın.

```bash
~$ pre-commit run --all-files
```