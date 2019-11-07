
var myArgs = process.argv.slice(2);

if (myArgs.length === 0) {
    console.log("No url passed in")
    return -1;
}

const HCCrawler = require('headless-chrome-crawler');
const siteUrl = myArgs[0];

let allImages = [];
let visitedUrls = [];
let linkCount = 0;
let linksLimit = 100;

(async () => {
  const crawler = await HCCrawler.launch({
    args: ['--no-sandbox'],
    evaluatePage: (() => ({
      images: $('img').map(function(){ return $(this).attr('src'); })
    })),
    onSuccess: (result => {
        if (result.result && result.result.images) {
            let images = result.result.images;
            delete images.length;
            delete images.prevObject;
            images = Object.values(images);
            images.forEach(f => {
                if (!allImages.includes(f))
                    allImages.push(f);
            })
        }
        result.links.forEach(href => {
            if ( href.includes(siteUrl) ) {
                if (!visitedUrls.includes(href) && linkCount <= linksLimit) {
                    visitedUrls.push(href);
                    crawler.queue(href);
                    linkCount++
                } 
            }
        })
    }),
  });
  await crawler.queue(siteUrl);
  await crawler.onIdle(); // Resolved when no queue is left
  await crawler.close(); // Close the crawler

  allImages = allImages.map(i => !i.includes(siteUrl) && !i.startsWith('http') ? siteUrl + i : i);
  console.log(allImages);
})();

