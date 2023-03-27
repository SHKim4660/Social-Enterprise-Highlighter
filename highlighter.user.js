// ==UserScript==
// @name        Social Enterprise Highlighter - coupang.com
// @namespace   Violentmonkey Scripts
// @match       https://www.coupang.com/np/search
// @grant       GM_xmlhttpRequest
// @version     1.0
// @author      hyc3573
// @description 2023. 3. 26. 오후 3:47:01
// ==/UserScript==

document.querySelectorAll("div.name").forEach(
    (name) => {
        name.style.backgroundColor = "#00ffff"

        var img = document.createElement("img")
        img.src = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.89XIMHLxI2RmF_M_QST1EwHaD4%26pid%3DApi&f=1&ipt=d52dd821ad764f8cd60fe165d1747a337e783625084c808026948c37b669dd4a&ipo=images"
        img.alt = "asdf"
        name.prepend(img)
        var link = name.closest("a").href
        console.log(link)

        GM_xmlhttpRequest({url: link,
                           method: "GET",
                           onload: (response) => {
                               if (response.status != 200) {return}

                               var vendor = response
                                   .responseXML
                                   .querySelector( "a.prod-sale-vendor-name")
                                   .textContent

                               if (!vendor) {return}

                               console.log(vendor)
                               var h1 = document.createElement("h1")
                               h1.innerText = `(${vendor})`

                               name.appendChild(h1)
                          }})

        // name.parentElement
    }
)
