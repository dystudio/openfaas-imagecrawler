# openfaas-imagecrawler

```bash
# deploy
faas-cli deploy -f stack.yml

# invoke
echo https://lotussoulstudios.com | faas-cli invoke openfaas-imagecrawler | jq
[
  "http://www.lotussoulstudios.com/wp-content/blogs.dir/60/files/2017/12/IMG_9453.jpg",
  "https://lotussoulstudios.com/wp-content/plugins/social-media-feather/synved-social/image/social/regular/64x64/facebook.png",
  "https://lotussoulstudios.com/wp-content/plugins/social-media-feather/synved-social/image/social/regular/64x64/youtube.png",
  "https://lotussoulstudios.com/wp-content/plugins/social-media-feather/synved-social/image/social/regular/64x64/twitter.png",
  "http://www.lotussoulstudios.com/wp-content/blogs.dir/60/files/2014/06/Door-of-Choice.jpg",
  "https://lotussoulstudios.com/wp-content/plugins/social-media-feather/synved-social/image/social/regular/64x64/mail.png",
  "https://lotussoulstudios.com/wp-content/plugins/social-media-feather/synved-social/image/social/regular/64x64/linkedin.png",
  "https://lotussoulstudios.com/wp-content/plugins/social-media-feather/synved-social/image/social/regular/64x64/tumblr.png",
  "https://lotussoulstudios.com/wp-content/plugins/social-media-feather/synved-social/image/social/regular/64x64/reddit.png",
  "http://www.lotussoulstudios.com/wp-content/blogs.dir/60/files/2018/02/IMG_0877.jpg",
  "https://lotussoulstudios.com/wp-content/plugins/social-media-feather/synved-social/image/social/regular/64x64/flickr.png",
  "https://lotussoulstudios.com/wp-content/plugins/social-media-feather/synved-social/image/social/regular/64x64/pinterest.png"
]
```
