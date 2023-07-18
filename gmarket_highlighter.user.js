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

function modifydiv(name, vendor, job) {
    // 제목 백그라운드 색상
    name.style.backgroundColor = "#00FFFF";
    name.style.display = "inline-block";
    name.style.padding = "5px";
    // name.style.backgroundClip = "content-box"
    name.style.borderRadius = "6px"

    var h1 = document.createElement("h1");
    h1.innerText = `${vendor}(${job})`;

    // 호버 창
    var hover = document.createElement("div");
    hover.innerText = `${vendor}(${job})`;
    hover.className = "socihihover";
    name.parentNode.insertBefore(hover, name.nextSibling);
}

// 호버 창 CSS
GM_addStyle(`
.socihihover {
  display: flex;
  justify-content: center;
  align-content: center;
  flex-direction: column;

  visibility: hidden;
  background-color: black;
  font-size: 16px;
  color: white;
  padding: 7px;
  border-radius: 6px;
  z-index: 9999;
  position: absolute;
}

div.box__item-title:hover ~ .socihihover {
  visibility: visible;
  height: 30px;
}`);

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










