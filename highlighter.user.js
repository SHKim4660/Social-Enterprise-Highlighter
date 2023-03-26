// ==UserScript==
// @name        Social Enterprise Highlighter - coupang.com
// @namespace   Violentmonkey Scripts
// @match       https://www.coupang.com/np/search
// @grant       none
// @version     1.0
// @author      hyc3573
// @description 2023. 3. 26. 오후 3:47:01
// ==/UserScript==

document.querySelectorAll("div.name").forEach(
  (name) => {name.style.backgroundColor = "#00ff00"}
)
