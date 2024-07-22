function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const handleLikeClick = (buttonId) => {
    console.log(buttonId);

    const likeButton = document.getElementById(buttonId);
    const likeIcon = likeButton.querySelector("i");

    const csrftoken = getCookie('csrftoken');
    // like-button-{{ post.id }}
    const postId = buttonId.split("-").pop();
    const url = postId + "/post_like"

    const xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", csrftoken);

    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                const data = JSON.parse(xhr.responseText);
                // 결과를 받고 html(좋아요 하트) 모습을 변경
                if (data.result === "like") {
                    likeIcon.classList.replace("fa-heart-o", "fa-heart");
                } else {
                    likeIcon.classList.replace("fa-heart", "fa-heart-o");
                }
            }
        }
    };

    xhr.send();
}