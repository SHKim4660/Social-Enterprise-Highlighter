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
    // name.appendChild(h1);

    var hover = document.createElement("div");
    hover.innerText = vendor;
    hover.className = "socihihover";
    // hover.style.display = none;
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
}

div.name:hover > .socihihover {
  visibility: visible;
}`);

document.querySelectorAll("div.name").forEach(
    (name) => {
        var img = document.createElement("img");
        img.src = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.89XIMHLxI2RmF_M_QST1EwHaD4%26pid%3DApi&f=1&ipt=d52dd821ad764f8cd60fe165d1747a337e783625084c808026948c37b669dd4a&ipo=images";
        img.alt = "asdf";
        // name.prepend(img)
        var link = name.closest("a").href;
        console.log(link);

        GM_xmlhttpRequest(
            {
                url: link,
                method: "GET",
                onload: (response) => {
                    if (response.status != 200) { return };

                    var vendor = response
                        .responseXML
                        .querySelector("text__seller")
                        .textContent;

                    if (!vendor) { return; };

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
