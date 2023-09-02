// ==UserScript==
// @name        New script - 11st.co.kr
// @namespace   Violentmonkey Scripts
// @match       https://search.11st.co.kr/pc/total-search
// @grant       GM_xmlhttpRequest
// @grant       GM_addStyle
// @version     1.0
// @author      hyc3573
// @description 8/23/2023, 8:49:14 AM
// ==/UserScript==

function getStyle() {
    GM_xmlhttpRequest(
        {
            url: "http://$HOST/style-1.css",
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

async function run () {
    document.querySelectorAll("a.c-card-item__anchor").forEach((a) => {
        let link = a.href

        console.log(link)

        GM_xmlhttpRequest(
            {
                url: link,
                method: "GET",
                onload: (response) => {
                    if (response.status != 200) { return };

                    let vendor = response.responseXML
                        .querySelector("table.prdc_detail_table").rows[5].cells[1].textContent;

                    console.log(vendor)

                    GM_xmlhttpRequest(
                        {
                            url: `http://$HOST/api/${vendor}`,
                            method: "GET",
                            onload: (response) => {
                                if (response.status != 200) { return; };
                                job = response.responseText;
                                console.log(job);

                                // a.style.background = "cyan"
                                let item_name = a.parentNode.querySelector("div.c-card-item__name")
                                item_name.classList.add("socihi-highlight")
                                let hover = document.createElement("div");
                                hover.innerText = `${vendor}(${job})`
                                hover.className = "socihi-hover-elem"
                                item_name.after(hover)
                                a.classList.add("socihi-hover-parent")
                            }
                        }
                    )
                }
            }
        )
    })
}

setTimeout(run, 2500)

setInterval(function () {
    getStyle();
}, 1000)
