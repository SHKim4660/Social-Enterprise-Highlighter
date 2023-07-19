// ==UserScript==
// @name        Social Enterprise Highlighter - gmarket.com
// @namespace   Violentmonkey Scripts
// @match       https://browse.gmarket.co.kr/search
// @resource    myStyle http://127.0.0.1:8081/style.css
// @grant       GM_xmlhttpRequest
// @grant       GM_addStyle
// @grant       GM_getResourceText
// @version     1.0.1
// @author      hyc3573
// @description 2023. 3. 26. 오후 3:47:01
// ==/UserScript==

function modifydiv(name, vendor, job) {
    // 제목 백그라운드 색상
    name.classList.add("socihihighlight")

    var h1 = document.createElement("h1");
    h1.innerText = `${vendor}(${job})`;

    // 호버 창
    var hover = document.createElement("div");
    hover.innerText = `${vendor}(${job})`;
    hover.className = "socihihover";
    name.parentNode.insertBefore(hover, name.nextSibling);
}

function getStyle() {
    GM_xmlhttpRequest(
        {
            url: "http://127.0.0.1:8081/style.css",
            method: "GET",
            onload: (response) => {
                if (response.status != 200) { return };

                var css = response.responseText;
                GM_addStyle(css);
            }
        }
    )
}

// GM_addStyle(GM_getResourceText('myStyle'));
getStyle();

document.querySelectorAll("div.box__item-title").forEach(
    (name) => {
        // 상품 링크
        var link = name.querySelector("a.link__item").href

        // 상품 링크로 http 리퀘스트 전송
        GM_xmlhttpRequest(
            {
                url: link,
                method: "GET",
                onload: (response) => {
                    // 에러시 스킵
                    if (response.status != 200) { return };

                    // 브랜드명 선택
                    var vendorspan = response
                        .responseXML
                        .querySelector("span.text__brand>span.text")

                    if (!vendorspan) { return; };

                    var vendor = vendorspan.textContent

                    console.log(vendor);

                    var is_social = false;
                    // api 리퀘스트 전송
                    GM_xmlhttpRequest(
                        {
                            url:
                                `http://localhost:8081/api/${vendor}`,
                            method: "GET",
                            onload: (response) => {
                                if (response.status != 200) { return; };
                                // response.status == 200이면 사회적 기업임
                                job =
                                    response.responseText// == "YEP"; // 여기서 Ture False 판단함

                                console.log(job);
                                modifydiv(name, vendor, response.responseText);
                            }
                        }
                    );
                }
            });
    }
);

setInterval(function() {
    getStyle();
}, 1000)
