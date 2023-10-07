// ==UserScript==
// @name        Social Enterprise Highlighter - coupang.com
// @namespace   Violentmonkey Scripts
// @match       https://www.coupang.com/np/search
// @grant       GM_xmlhttpRequest
// @grant       GM_addStyle
// @version     1.0
// @author      hyc3573
// @description 8/21/2023, 1:22:21 PM
// ==/UserScript==

function modifydiv(name, vendor, job) {
    console.log("mod")
    
    // 제목 백그라운드 색상
    name.classList.add("socihihighlight")

    let h1 = document.createElement("h1");
    h1.innerText = `${vendor}(${job})`;

    // 호버 창
    let hover = document.createElement("div");
    hover.innerText = `${vendor}(${job})`;
    hover.className = "socihihover";
    name.parentNode.insertBefore(hover, name.nextSibling);
}

function getStyle() {
    GM_xmlhttpRequest(
        {
            url: "http://$HOST/style-g.css",
            method: "GET",
            onload: (response) => {
                if (response.status != 200) { return };

                let css = response.responseText;
                GM_addStyle(css);
            }
        }
    )
}

getStyle();

document.querySelectorAll("div.name").forEach(
    (name) => {
        let product_link = name
            .parentNode
            .parentNode
            .parentNode
            .parentNode
            .href;
        console.log(product_link)

        GM_xmlhttpRequest(
            {
                url: product_link,
                method: "GET",
                onload: (response) => {
                    if (response.status != 200) { return };

                    let vendorname = response.responseXML.querySelector("a.prod-brand-name").textContent.trim();

                    console.log(vendorname);

                    let job = "asdf";
                    console.log(job);

                    modifydiv(name, vendorname, job);

                    // GM_xmlhttpRequest(
                    //     {
                    //         url: `http://$HOST/api/${vendorname}`,
                    //         method: "GET",
                    //         onload: (response) => {
                    //             if (response.status != 200) 
                    //             {
                    //                 // return;
                    //             }

                    //             job = reponse.responseText;
                    //             console.log(job)

                    //             debug();
                    //             modifydiv(name, vendor, job);
                    //         }
                    //     }
                    // )
                }
            }
        )
    }
)

setInterval(function () {
    getStyle();
}, 1000)
