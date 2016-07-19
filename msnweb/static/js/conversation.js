function get_conversation_version(conversation_id) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/conversation/' + conversation_id + '/version', false);
    xhr.send(null);
    return JSON.parse(xhr.responseText).version;
}

function update_messages(conversation_id, dom) {
    if (!dom.hasAttribute('version')) {
        dom.setAttribute('version', '-1');
    }

    var current_version = get_conversation_version(conversation_id);

    if (current_version != parseInt(dom.getAttribute('version'))) {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == XMLHttpRequest.DONE) {
                dom.innerHTML = xhr.responseText;
                dom.scrollTop = dom.scrollHeight+1;
            }
        }
        xhr.open('GET', '/api/conversation/' + conversation_id, true);
        xhr.send(null);

        dom.setAttribute('version', current_version);
    }
}

function send_message(conversation_id, body) {
    var http = new XMLHttpRequest();
    var url = "/api/conversation/" + conversation_id + "/send";
    var body = document.getElementById('send-body').value;
    var params = "body="+body;
    http.open("POST", url, true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            //input_dom.value = '';
        }
    }
    http.send(params);
}
