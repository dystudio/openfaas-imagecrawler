# openfaas-imagecrawler

```bash
# deploy
faas-cli deploy -f stack.yml

# invoke
echo https://lotussoulstudios.com | faas-cli invoke openfaas-imagecrawler --async --header "X-Callback-Url=http://192.168.0.22:9999"
```