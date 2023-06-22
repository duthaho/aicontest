var JBase = (function () {
  function set_url_param(url, param, paramVal) {
    var TheAnchor = null;
    var newAdditionalURL = "";
    var tempArray = url.split("?");
    var baseURL = tempArray[0];
    var additionalURL = tempArray[1];
    var temp = "";
    var tmpAnchor = baseURL.split("#");
    var TheParams = tmpAnchor[0];

    if (additionalURL) {
      tmpAnchor = additionalURL.split("#");
      TheParams = tmpAnchor[0];
      TheAnchor = tmpAnchor[1];
      if (TheAnchor) additionalURL = TheParams;

      tempArray = additionalURL.split("&");

      for (i = 0; i < tempArray.length; i++) {
        if (tempArray[i].split("=")[0] != param) {
          newAdditionalURL += temp + tempArray[i];
          temp = "&";
        }
      }
    } else {
      TheAnchor = tmpAnchor[1];

      if (TheParams) {
        baseURL = TheParams;
      }
    }

    if (TheAnchor) paramVal += "#" + TheAnchor;

    var rows_txt = temp + "" + param + "=" + encodeURIComponent(paramVal);
    return baseURL + "?" + newAdditionalURL + rows_txt;
  }

  function get_csrftoken() {
    var el = document.getElementsByName("csrfmiddlewaretoken");
    if (el && el.length) {
      return el[0].value;
    }
  }

  function send(url, params, output) {
    var defaultParams = {
      showLoading: true,
    };
    var outputParams = output || false;
    params = $.extend({}, defaultParams, params);
    params.beforeSend = function (xhr, settings) {
      xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
      var csrftoken = get_csrftoken();
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    };
    var requestParams = {
      type: params.type || "POST",
      statusCode: {
        404: function () {},
      },
      context: params.context || null,
    };

    if (params.timeout) {
      requestParams["timeout"] = params.timeout;
    }

    if (params.data) {
      requestParams.data = params.data;
    } else {
      requestParams.data = {};
    }

    if (outputParams) {
      requestParams.dataType = outputParams;
    }
    if (params.xhrFields) {
      requestParams.xhrFields = {
        withCredentials: true,
      };
    }
    requestParams.success = function (data) {
      if (params.success && $.isFunction(params.success)) {
        if (typeof data !== "object") {
          try {
            data = JSON.parse(data);
          } catch (e) {}
        }
        params.success(data);
      }
    };
    requestParams.complete = function (xhr, textStatus) {
      if (params.complete && $.isFunction(params.complete)) {
        params.complete(xhr, textStatus);
      }
    };
    if (params.beforeSend && $.isFunction(params.beforeSend)) {
      requestParams.beforeSend = function (xhr, settings) {
        params.beforeSend(xhr, settings);
      };
    }
    if (params.hasOwnProperty("processData")) {
      requestParams.processData = params.processData;
    }
    if (params.hasOwnProperty("contentType")) {
      requestParams.contentType = params.contentType;
    }
    var request = jQuery.ajax(url, requestParams);
    return request;
  }

  return {
    send,
    get_csrftoken,
    set_url_param,
  };
})();
