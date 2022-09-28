# Recon NFT based on browser Fingerprint

Following the same steps detailed by [Convex Labs]() in the [Recon NFT Medium post](https://medium.com/@convexlabs/this-nft-logs-your-ip-address-7f6f9cf2376e), I was able to inject a fingerprinting JavaScript library into an NFT's metadata.

Here is an NFT on the Goerli test network that can be viewed on OpenSea: https://testnets.opensea.io/assets/goerli/0xcab4aa1f5504d7eefa78ee040d8b733499c20e1a/2
Your browser's fingerprint, and a detailed dump of the tracked features, will be displayed in the Developer Console.

> Note: The fingerprints are not saved anywhere

This fingerprint can be the basis for a dynamic display on the NFT on the Marketplace, and raise awareness about Browser Fingerprinting while fitting the theme of **Vigilante NFTs**. 

The following are display ideas that revolve around the fingerprint:
1. NFTs unlocked with Anonymous Browser Fingerprints only
2. NFTs featuring characters that reflect the anonymity of the browser
3. NFTs that detect bots and crawlers


## How much anonymous is a fingerprint?

> https://amiunique.org/

This compares a browser's fingerprint against a set of 840827 saved fingerprints to determine if you are unique or not.
Evidently, the aim is not to be identifiable, and blend in with the multitude of browser/OS/cookies that are the most common.


## Fingerprint dump

> This has been heavily changed for anonymity's sake

```json
{
  "confidence": {
    "score": 0.7,
    "comment": "0.997 if upgrade to Pro: https://fpjs.dev/pro"
  },
  "components": {
    "fonts": {
      "error": {},
      "duration": 17
    },
    "domBlockers": {
      "duration": 3
    },
    "fontPreferences": {
      "error": {},
      "duration": 6
    },
    "audio": {
      "value": 24.73833402246237,
      "duration": 38
    },
    "screenFrame": {
      "value": [
        30,
        0,
        0,
        70
      ],
      "duration": 1
    },
    "osCpu": {
      "value": "Linux x86_64",
      "duration": 0
    },
    "languages": {
      "value": [
        [
          "en-GB"
        ]
      ],
      "duration": 1
    },
    "colorDepth": {
      "value": 24,
      "duration": 0
    },
    "deviceMemory": {
      "duration": 0
    },
    "screenResolution": {
      "value": [
        1920,
        1080
      ],
      "duration": 0
    },
    "hardwareConcurrency": {
      "value": 8,
      "duration": 0
    },
    "timezone": {
      "value": "Europe/Paris",
      "duration": 26
    },
    "sessionStorage": {
      "value": true,
      "duration": 0
    },
    "localStorage": {
      "value": true,
      "duration": 0
    },
    "indexedDB": {
      "value": true,
      "duration": 0
    },
    "openDatabase": {
      "value": false,
      "duration": 0
    },
    "cpuClass": {
      "duration": 0
    },
    "platform": {
      "value": "Linux x86_64",
      "duration": 0
    },
    "plugins": {
      "value": [
        {
          "name": "PDF Viewer",
          "description": "Portable Document Format",
          "mimeTypes": [
            {
              "type": "application/pdf",
              "suffixes": "pdf"
            },
            {
              "type": "text/pdf",
              "suffixes": "pdf"
            }
          ]
        },
        ...
        ...
        {
          "name": "WebKit built-in PDF",
          "description": "Portable Document Format",
          "mimeTypes": [
            {
              "type": "application/pdf",
              "suffixes": "pdf"
            },
            ....
          ]
        }
      ],
      "duration": 1
    },
    "canvas": {
      "value": {
        "winding": true,
        "geometry": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHo.....gg=="
      },
      "duration": 31
    },
    "touchSupport": {
      "value": {
        "maxTouchPoints": 0,
        "touchEvent": false,
        "touchStart": false
      },
      "duration": 0
    },
    "vendor": {
      "value": "",
      "duration": 0
    },
    "vendorFlavors": {
      "value": [],
      "duration": 1
    },
    "cookiesEnabled": {
      "value": false,
      "duration": 1
    },
    "colorGamut": {
      "duration": 0
    },
    "invertedColors": {
      "duration": 0
    },
    "forcedColors": {
      "value": false,
      "duration": 0
    },
    "monochrome": {
      "value": 0,
      "duration": 0
    },
    "contrast": {
      "value": 0,
      "duration": 0
    },
    "reducedMotion": {
      "value": false,
      "duration": 0
    },
    "hdr": {
      "value": false,
      "duration": 0
    },
    "math": {
      "value": {
          ....
      },
      "duration": 1
    }
  },
  "version": "3.3.6"
}
```