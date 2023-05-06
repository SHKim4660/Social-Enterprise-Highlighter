// ==UserScript==
// @name        Social Enterprise Highlighter - gmarket.com
// @namespace   Violentmonkey Scripts
// @match       https://browse.gmarket.co.kr/search
// @grant       GM_xmlhttpRequest
// @grant       GM_addStyle
// @version     1.0.1
// @author      hyc3573
// @description 2023. 3. 26. 오후 3:47:01
// ==/UserScript==

function modifydiv(name, vendor) {
    name.style.backgroundColor = "#00ffff";

    var h1 = document.createElement("h1");
    h1.innerText = `(${vendor})`;

    var hover = document.createElement("div");
    hover.innerText = vendor;
    hover.className = "socihihover";
    name.appendChild(hover);
}

GM_addStyle(`
.socihihover {
  visibility: hidden;
  width: 120px;
  background-color: black;
  color: #fff;
  text-align: center;
  padding: 5px 0;
  border-radius: 6px;
  height: 0px;
}

div.box__item-title:hover > .socihihover {
  visibility: visible;
  height: 30px;
}`);

document.querySelectorAll("div.box__item-title").forEach(
    (name) => {

        var link = name.querySelector("a.link__item").href

        GM_xmlhttpRequest(
            {
                url: link,
                method: "GET",
                onload: (response) => {
                    if (response.status != 200) { return };

                    var vendorspan = response
                        .responseXML
                        .querySelector("span.text__brand>span.text")

                    if (!vendorspan) { return; };

                    var vendor = vendorspan.textContent

                    console.log(vendor);

                    var is_social = false;
                    GM_xmlhttpRequest(
                        {
                            url:
                                `http://localhost:8081/api/${vendor}`,
                            method: "GET",
                            onload: (response) => {
                                if (response.status != 200) { return; };
                                is_social =
                                    response.responseText == "YEP";

                                console.log(is_social);
                                if (is_social) {
                                    modifydiv(name, vendor);
                                }
                            }
                        }
                    );
                }
            });
    }
);
