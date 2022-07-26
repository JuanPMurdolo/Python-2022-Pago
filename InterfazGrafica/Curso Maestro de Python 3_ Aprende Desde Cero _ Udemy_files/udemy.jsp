Array.prototype.filter||(Array.prototype.filter=function(t,e){"use strict";if("Function"!=typeof t&&"function"!=typeof t||!this)throw new TypeError;var r=this.length>>>0,o=new Array(r),n=this,l=0,i=-1;if(void 0===e)for(;++i!==r;)i in this&&t(n[i],i,n)&&(o[l++]=n[i]);else for(;++i!==r;)i in this&&t.call(e,n[i],i,n)&&(o[l++]=n[i]);return o.length=l,o}),Array.prototype.forEach||(Array.prototype.forEach=function(t){var e,r;if(null==this)throw new TypeError('"this" is null or not defined');var o=Object(this),n=o.length>>>0;if("function"!=typeof t)throw new TypeError(t+" is not a function");for(arguments.length>1&&(e=arguments[1]),r=0;r<n;){var l;r in o&&(l=o[r],t.call(e,l,r,o)),r++}}),window.NodeList&&!NodeList.prototype.forEach&&(NodeList.prototype.forEach=Array.prototype.forEach),Array.prototype.indexOf||(Array.prototype.indexOf=function(t,e){var r;if(null==this)throw new TypeError('"this" is null or not defined');var o=Object(this),n=o.length>>>0;if(0===n)return-1;var l=0|e;if(l>=n)return-1;for(r=Math.max(l>=0?l:n-Math.abs(l),0);r<n;){if(r in o&&o[r]===t)return r;r++}return-1}),document.getElementsByClassName||(document.getElementsByClassName=function(t){var e,r,o,n=document,l=[];if(n.querySelectorAll)return n.querySelectorAll("."+t);if(n.evaluate)for(r=".//*[contains(concat(' ', @class, ' '), ' "+t+" ')]",e=n.evaluate(r,n,null,0,null);o=e.iterateNext();)l.push(o);else for(e=n.getElementsByTagName("*"),r=new RegExp("(^|\\s)"+t+"(\\s|$)"),o=0;o<e.length;o++)r.test(e[o].className)&&l.push(e[o]);return l}),document.querySelectorAll||(document.querySelectorAll=function(t){var e,r=document.createElement("style"),o=[];for(document.documentElement.firstChild.appendChild(r),document._qsa=[],r.styleSheet.cssText=t+"{x-qsa:expression(document._qsa && document._qsa.push(this))}",window.scrollBy(0,0),r.parentNode.removeChild(r);document._qsa.length;)(e=document._qsa.shift()).style.removeAttribute("x-qsa"),o.push(e);return document._qsa=null,o}),document.querySelector||(document.querySelector=function(t){var e=document.querySelectorAll(t);return e.length?e[0]:null}),Object.keys||(Object.keys=function(){"use strict";var t=Object.prototype.hasOwnProperty,e=!{toString:null}.propertyIsEnumerable("toString"),r=["toString","toLocaleString","valueOf","hasOwnProperty","isPrototypeOf","propertyIsEnumerable","constructor"],o=r.length;return function(n){if("function"!=typeof n&&("object"!=typeof n||null===n))throw new TypeError("Object.keys called on non-object");var l,i,s=[];for(l in n)t.call(n,l)&&s.push(l);if(e)for(i=0;i<o;i++)t.call(n,r[i])&&s.push(r[i]);return s}}()),"function"!=typeof String.prototype.trim&&(String.prototype.trim=function(){return this.replace(/^\s+|\s+$/g,"")}),String.prototype.replaceAll||(String.prototype.replaceAll=function(t,e){return"[object regexp]"===Object.prototype.toString.call(t).toLowerCase()?this.replace(t,e):this.replace(new RegExp(t,"g"),e)}),window.hasOwnProperty=window.hasOwnProperty||Object.prototype.hasOwnProperty;
if (typeof usi_commons === 'undefined') {
	usi_commons = {
		
		debug: location.href.indexOf("usidebug") != -1 || location.href.indexOf("usi_debug") != -1,
		
		log:function(msg) {
			if (usi_commons.debug) {
				try {
					if (msg instanceof Error) {
						console.log(msg.name + ': ' + msg.message);
					} else {
						console.log.apply(console, arguments);
					}
				} catch(err) {
					usi_commons.report_error_no_console(err);
				}
			}
		},
		log_error: function(msg) {
			if (usi_commons.debug) {
				try {
					if (msg instanceof Error) {
						console.log('%c USI Error:', usi_commons.log_styles.error, msg.name + ': ' + msg.message);
					} else {
						console.log('%c USI Error:', usi_commons.log_styles.error, msg);
					}
				} catch(err) {
					usi_commons.report_error_no_console(err);
				}
			}
		},
		log_success: function(msg) {
			if (usi_commons.debug) {
				try {
					console.log('%c USI Success:', usi_commons.log_styles.success, msg);
				} catch(err) {
					usi_commons.report_error_no_console(err);
				}
			}
		},
		dir:function(obj) {
			if (usi_commons.debug) {
				try {
					console.dir(obj);
				} catch(err) {
					usi_commons.report_error_no_console(err);
				}
			}
		},
		log_styles: {
			error: 'color: red; font-weight: bold;',
			success: 'color: green; font-weight: bold;'
		},
		domain: "https://www.upsellit.com",
		cdn: "https://www.upsellit.com",
		is_mobile: (/iphone|ipod|ipad|android|blackberry|mobi/i).test(navigator.userAgent.toLowerCase()),
		device: (/iphone|ipod|ipad|android|blackberry|mobi/i).test(navigator.userAgent.toLowerCase()) ? 'mobile' : 'desktop',
		gup:function(name) {
			try {
				name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
				var regexS = "[\\?&]" + name + "=([^&#\\?]*)";
				var regex = new RegExp(regexS);
				var results = regex.exec(window.location.href);
				if (results == null) return "";
				else return results[1];
			} catch (e) {
				usi_commons.report_error(e);
			}
		},
		load_script:function(source, callback, nocache) {
			try {
				if (source.indexOf("//www.upsellit.com") == 0) source = "https:"+source; //upgrade non-secure requests
				var docHead = document.getElementsByTagName("head")[0];
				if (top.location != location) docHead = parent.document.getElementsByTagName("head")[0];
				var newScript = document.createElement('script');
				newScript.type = 'text/javascript';
				var usi_appender = "";
				if (!nocache && source.indexOf("_pixel.jsp") == -1 && source.indexOf("_throttle.jsp") == -1 && source.indexOf("metro") == -1 && source.indexOf("_suppress") == -1 && source.indexOf("product_recommendations.jsp") == -1 && source.indexOf("_pid.jsp") == -1 && source.indexOf("_zips") == -1) {
					usi_appender = (source.indexOf("?")==-1?"?":"&");
					if (source.indexOf("pv2.js") != -1) usi_appender = "%7C";
					usi_appender += "si=" + usi_commons.get_sess();
				}
				newScript.src = source + usi_appender;
				if (typeof callback == "function") {
					newScript.onload = function() {
						try {
							callback();
						} catch (e) {
							usi_commons.report_error(e);
						}
					};
				}
				docHead.appendChild(newScript);
			} catch (e) {
				usi_commons.report_error(e);
			}
		},
		load_display:function(usiQS, usiSiteID, usiKey, callback) {
			try {
				usiKey = usiKey || "";
				var source = usi_commons.domain + "/launch.jsp?qs=" + usiQS + "&siteID=" + usiSiteID + "&keys=" + usiKey;
				usi_commons.load_script(source, callback);
			} catch (e) {
				usi_commons.report_error(e);
			}
		},
		load_view:function(usiHash, usiSiteID, usiKey, callback) {
			try {
				if (typeof(usi_force) != "undefined" || location.href.indexOf("usi_force") != -1 || (usi_cookies.get("usi_sale") == null && usi_cookies.get("usi_launched") == null && usi_cookies.get("usi_launched"+usiSiteID) == null)) {
					usiKey = usiKey || "";
					var usi_append = "";
					if (usi_commons.gup("usi_force_date") != "") usi_append = "&usi_force_date=" + usi_commons.gup("usi_force_date");
					else if (typeof usi_cookies !== 'undefined' && usi_cookies.get("usi_force_date") != null) usi_append = "&usi_force_date=" + usi_cookies.get("usi_force_date");
					if (usi_commons.debug) usi_append += "&usi_referrer="+encodeURIComponent(location.href);
					var source = usi_commons.domain + "/view.jsp?hash=" + usiHash + "&siteID=" + usiSiteID + "&keys=" + usiKey + usi_append;
					if (typeof(usi_commons.last_view) !== "undefined" && usi_commons.last_view == usiSiteID+"_"+usiKey) return;
					usi_commons.last_view = usiSiteID+"_"+usiKey;
					if (typeof usi_js !== 'undefined' && typeof usi_js.cleanup === 'function') usi_js.cleanup();
					usi_commons.load_script(source, callback);
				}
			} catch (e) {
				usi_commons.report_error(e);
			}
		},
		remove_loads:function() {
			try {
				if (document.getElementById("usi_obj") != null) {
					document.getElementById("usi_obj").parentNode.parentNode.removeChild(document.getElementById("usi_obj").parentNode);
				}
				if (typeof(usi_commons.usi_loads) !== "undefined") {
					for (var i in usi_commons.usi_loads) {
						if (document.getElementById("usi_"+i) != null) {
							document.getElementById("usi_"+i).parentNode.parentNode.removeChild(document.getElementById("usi_"+i).parentNode);
						}
					}
				}
			} catch (e) {
				usi_commons.report_error(e);
			}
		},
		load:function(usiHash, usiSiteID, usiKey, callback){
			try {
				if (typeof(window["usi_" + usiSiteID]) !== "undefined") return;
				usiKey = usiKey || "";
				var usi_append = "";
				if (usi_commons.gup("usi_force_date") != "") usi_append = "&usi_force_date=" + usi_commons.gup("usi_force_date");
				else if (typeof usi_cookies !== 'undefined' && usi_cookies.get("usi_force_date") != null) usi_append = "&usi_force_date=" + usi_cookies.get("usi_force_date");
				if (usi_commons.debug) usi_append += "&usi_referrer="+encodeURIComponent(location.href);
				var source = usi_commons.domain + "/usi_load.jsp?hash=" + usiHash + "&siteID=" + usiSiteID + "&keys=" + usiKey + usi_append;
				usi_commons.load_script(source, callback);
				if (typeof(usi_commons.usi_loads) === "undefined") {
					usi_commons.usi_loads = {};
				}
				usi_commons.usi_loads[usiSiteID] = usiSiteID;
			} catch (e) {
				usi_commons.report_error(e);
			}
		},
		load_precapture:function(usiQS, usiSiteID, callback) {
			try {
				var source = usi_commons.domain + "/hound/monitor.jsp?qs=" + usiQS + "&siteID=" + usiSiteID + "&domain=" + encodeURIComponent(usi_commons.domain);
				usi_commons.load_script(source, callback);
			} catch (e) {
				usi_commons.report_error(e);
			}
		},
		load_mail:function(qs, siteID, callback) {
			try {
				var source = usi_commons.domain + "/mail.jsp?qs=" + qs + "&siteID=" + siteID + "&domain=" + encodeURIComponent(usi_commons.domain);
				usi_commons.load_script(source, callback);
			} catch (e) {
				usi_commons.report_error(e);
			}
		},
		send_prod_rec:function(siteID, info, real_time) {
			var result = false;
			try {
				if (document.getElementsByTagName("html").length > 0 && document.getElementsByTagName("html")[0].className != null && document.getElementsByTagName("html")[0].className.indexOf("translated") != -1) {
					//Ignore translated pages
					return false;
				}
				var data = [siteID, info.name, info.link, info.pid, info.price, info.image];
				if (data.indexOf(undefined) == -1) {
					var queryString = [siteID, info.name.replace(/\|/g, "&#124;"), info.link, info.pid, info.price, info.image].join("|") + "|";
					if (info.extra) queryString += info.extra + "|";
					var filetype = real_time ? "jsp" : "js";
					usi_commons.load_script(usi_commons.domain + "/active/pv2." + filetype + "?" + encodeURIComponent(queryString));
					result = true;
				}
			} catch (e) {
				usi_commons.report_error(e);
				result = false;
			}
			return result;
		},
		report_error:function(err) {
			if (err == null) return;
			if (typeof err === 'string') err = new Error(err);
			if (!(err instanceof Error)) return;
			if (typeof(usi_commons.error_reported) !== "undefined") {
				return;
			}
			usi_commons.error_reported = true;
			if (location.href.indexOf('usishowerrors') !== -1) throw err;
			else usi_commons.load_script(usi_commons.domain + '/err.jsp?oops=' + encodeURIComponent(err.message) + '-' + encodeURIComponent(err.stack) + "&url=" + encodeURIComponent(location.href));
			usi_commons.log_error(err.message);
			usi_commons.dir(err);
		},
		report_error_no_console:function(err) {
			if (err == null) return;
			if (typeof err === 'string') err = new Error(err);
			if (!(err instanceof Error)) return;
			if (typeof(usi_commons.error_reported) !== "undefined") {
				return;
			}
			usi_commons.error_reported = true;
			if (location.href.indexOf('usishowerrors') !== -1) throw err;
			else usi_commons.load_script(usi_commons.domain + '/err.jsp?oops=' + encodeURIComponent(err.message) + '-' + encodeURIComponent(err.stack) + "&url=" + encodeURIComponent(location.href));
		},
		gup_or_get_cookie: function(name, expireSeconds, forceCookie) {
			try {
				if (typeof usi_cookies === 'undefined') {
					usi_commons.log_error('usi_cookies is not defined');
					return;
				}
				expireSeconds = (expireSeconds || usi_cookies.expire_time.day);
				if (name == "usi_enable") expireSeconds = usi_cookies.expire_time.hour;
				var value = null;
				var qsValue = usi_commons.gup(name);
				if (qsValue !== '') {
					value = qsValue;
					usi_cookies.set(name, value, expireSeconds, forceCookie);
				} else {
					value = usi_cookies.get(name);
				}
				return (value || '');
			} catch (e) {
				usi_commons.report_error(e);
			}
		},
		get_sess: function() {
			var usi_si = null;
			if (typeof(usi_cookies) === "undefined") return "";
			try {
				if (usi_cookies.get('usi_si') == null) {
					var usi_rand_str = Math.random().toString(36).substring(2);
					if (usi_rand_str.length > 6) usi_rand_str = usi_rand_str.substring(0, 6);
					usi_si = usi_rand_str + "_" + Math.round((new Date()).getTime() / 1000);
					usi_cookies.set('usi_si', usi_si, 24*60*60);
					return usi_si;
				}
				if (usi_cookies.get('usi_si') != null) usi_si = usi_cookies.get('usi_si');
				usi_cookies.set('usi_si', usi_si, 24*60*60);
			} catch(err) {
				usi_commons.report_error(err);
			}
			return usi_si;
		},
		get_id: function() {
			var usi_id = null;
			try {
				if (usi_cookies.get('usi_v') == null && usi_cookies.get('usi_id') == null) {
					var usi_rand_str = Math.random().toString(36).substring(2);
					if (usi_rand_str.length > 6) usi_rand_str = usi_rand_str.substring(0, 6);
					usi_id = usi_rand_str + "_" + Math.round((new Date()).getTime() / 1000);
					usi_cookies.set('usi_id', usi_id, 30 * 86400, true);
					return usi_id;
				}
				if (usi_cookies.get('usi_v') != null) usi_id = usi_cookies.get('usi_v');
				if (usi_cookies.get('usi_id') != null) usi_id = usi_cookies.get('usi_id');
				usi_cookies.set('usi_id', usi_id, 30 * 86400, true);
			} catch(err) {
				usi_commons.report_error(err);
			}
			return usi_id;
		},
		load_session_data: function(extended) {
			try {
				if (usi_cookies.get_json("usi_session_data") == null && usi_cookies.get("usi_session_data") != null) {
					usi_commons.load_script(usi_commons.domain + '/launch/blank.jsp?json_err='+encodeURIComponent(usi_cookies.get("usi_session_data")));
				}
				if (usi_cookies.get_json("usi_session_data") == null) {
					usi_commons.load_script(usi_commons.domain + '/utility/session_data.jsp?extended=' + (extended?"true":"false"));
				} else {
					usi_app.session_data = usi_cookies.get_json("usi_session_data");
					if (typeof(usi_app.session_data_callback) !== "undefined") {
						usi_app.session_data_callback();
					}
				}
			} catch(err) {
				usi_commons.report_error(err);
			}
		}
	};
	setTimeout(function() {
		try {
			if (usi_commons.gup_or_get_cookie("usi_debug") != "") usi_commons.debug = true;
			if (usi_commons.gup_or_get_cookie("usi_qa") != "") {
				usi_commons.domain = usi_commons.cdn = "https://prod.upsellit.com";
			}
		} catch(err) {
			usi_commons.report_error(err);
		}
	}, 1000);
}

if (typeof usi_app === 'undefined') {
	try {
		if("undefined"==typeof usi_cookies&&(usi_cookies={expire_time:{minute:60,hour:3600,two_hours:7200,four_hours:14400,day:86400,week:604800,two_weeks:1209600,month:2592e3,year:31536e3,never:31536e4},max_cookies_count:15,max_cookie_length:1e3,update_window_name:function(h,a,i){try{var f=-1;if(-1!=i){var g=new Date;g.setTime(g.getTime()+1e3*i),f=g.getTime()}var j=window.top||window,k=0;null!=a&& -1!=a.indexOf("=")&&(a=a.replace(new RegExp("=","g"),"USIEQLS")),null!=a&& -1!=a.indexOf(";")&&(a=a.replace(new RegExp(";","g"),"USIPRNS"));for(var d=j.name.split(";"),e="",c=0;c<d.length;c++){var b=d[c].split("=");3==b.length?(b[0]==h&&(b[1]=a,b[2]=f,k=1),null!=b[1]&&"null"!=b[1]&&(e+=b[0]+"="+b[1]+"="+b[2]+";")):""!=d[c]&&(e+=d[c]+";")}0==k&&(e+=h+"="+a+"="+f+";"),j.name=e}catch(l){}},flush_window_name:function(f){try{for(var c=window.top||window,b=c.name.split(";"),d="",a=0;a<b.length;a++){var e=b[a].split("=");3==e.length&&(0==e[0].indexOf(f)||(d+=b[a]+";"))}c.name=d}catch(g){}},get_from_window_name:function(d){try{for(var a,e=(window.top||window).name.split(";"),c=0;c<e.length;c++){var b=e[c].split("=");if(3==b.length){if(b[0]==d&&(a=b[1],-1!=a.indexOf("USIEQLS")&&(a=a.replace(/USIEQLS/g,"=")),-1!=a.indexOf("USIPRNS")&&(a=a.replace(/USIPRNS/g,";")),!("-1"!=b[2]&&0>usi_cookies.datediff(b[2]))))return[a,b[2]]}else if(2==b.length&&b[0]==d)return a=b[1],-1!=a.indexOf("USIEQLS")&&(a=a.replace(/USIEQLS/g,"=")),-1!=a.indexOf("USIPRNS")&&(a=a.replace(/USIPRNS/g,";")),[a,new Date().getTime()+6048e5]}}catch(f){}return null},datediff:function(a){return a-new Date().getTime()},count_cookies:function(a){return a=a||"usi_",usi_cookies.search_cookies(a).length},root_domain:function(){try{var a=document.domain.split("."),b=a[a.length-1];if("com"==b||"net"==b||"org"==b||"us"==b||"co"==b||"ca"==b)return a[a.length-2]+"."+a[a.length-1]}catch(c){}return document.domain},create_cookie:function(f,g,b){if(!1!==navigator.cookieEnabled){var c="";if(-1!=b){var a=new Date;a.setTime(a.getTime()+1e3*b),c="; expires="+a.toGMTString()}var d="samesite=none;";0==location.href.indexOf("https://")&&(d+="secure;");var e=usi_cookies.root_domain();"undefined"!=typeof usi_parent_domain&& -1!=document.domain.indexOf(usi_parent_domain)&&(e=usi_parent_domain),document.cookie=f+"="+encodeURIComponent(g)+c+"; path=/;domain="+e+"; "+d}},read_cookie:function(e){if(!1===navigator.cookieEnabled)return null;var d=e+"=",b=[];try{b=document.cookie.split(";")}catch(f){}for(var c=0;c<b.length;c++){for(var a=b[c];" "==a.charAt(0);)a=a.substring(1,a.length);if(0==a.indexOf(d))return decodeURIComponent(a.substring(d.length,a.length))}return null},del:function(a){usi_cookies.set(a,null,-100);try{null!=localStorage&&localStorage.removeItem(a),null!=sessionStorage&&sessionStorage.removeItem(a)}catch(b){}},get_ls:function(b){try{var a=localStorage.getItem(b);if(null!=a){if(0==a.indexOf("{")&& -1!=a.indexOf("usi_expires")){var c=JSON.parse(a);if(new Date().getTime()>c.usi_expires)return localStorage.removeItem(b),null;a=c.value}return decodeURIComponent(a)}}catch(d){}return null},get:function(b){var a=null;try{if(null!=localStorage&&(a=usi_cookies.get_ls(b),null!=a))return a;if(null!=sessionStorage&&(a=sessionStorage.getItem(b),null!=a))return decodeURIComponent(a)}catch(d){}var c=usi_cookies.get_from_window_name(b);if(null!=c&&c.length>1)try{a=decodeURIComponent(c[0])}catch(e){return c[0]}else a=usi_cookies.read_cookie(b);return a},get_json:function(c){var b=null,a=usi_cookies.get(c);if(null==a)return null;try{b=JSON.parse(a)}catch(d){a=a.replace(/\\"/g,'"');try{b=JSON.parse(JSON.parse(a))}catch(e){try{b=JSON.parse(a)}catch(f){}}}return b},search_cookies:function(a){a=a||"";var b=[];return document.cookie.split(";").forEach(function(d){var c=d.split("=")[0].trim();(""===a||0===c.indexOf(a))&&b.push(c)}),b},set:function(b,a,c,d){"undefined"!=typeof usi_nevercookie&&(d=!1),void 0===c&&(c=-1);try{a=a.replace(/(\r\n|\n|\r)/gm,"")}catch(g){}"undefined"==typeof usi_windownameless&&usi_cookies.update_window_name(b+"",a+"",c);try{if(c>0&&null!=localStorage){var e=new Date,f={value:a,usi_expires:e.getTime()+1e3*c};localStorage.setItem(b,JSON.stringify(f))}else null!=sessionStorage&&sessionStorage.setItem(b,a)}catch(h){}if(d||null==a){if(null!=a){if(null==usi_cookies.read_cookie(b)&&!d&&usi_cookies.search_cookies("usi_").length+1>usi_cookies.max_cookies_count){usi_cookies.report_error('Set cookie "'+b+'" failed. Max cookies count is '+usi_cookies.max_cookies_count);return}if(a.length>usi_cookies.max_cookie_length){usi_cookies.report_error('Cookie "'+b+'" truncated ('+a.length+"). Max single-cookie length is "+usi_cookies.max_cookie_length);return}}usi_cookies.create_cookie(b,a,c)}},set_json:function(a,b,c,d){var e=JSON.stringify(b).replace(/^"/,"").replace(/"$/,"");usi_cookies.set(a,e,c,d)},flush:function(b){b=b||"usi_";var c,d,e,f=document.cookie.split(";");for(c=0;c<f.length;c++)0==(d=f[c]).trim().toLowerCase().indexOf(b)&&(e=d.trim().split("=")[0],usi_cookies.del(e));usi_cookies.flush_window_name(b);try{if(null!=localStorage)for(var a in localStorage)0==a.indexOf("usi_")&&localStorage.removeItem(a);if(null!=sessionStorage)for(var a in sessionStorage)0==a.indexOf("usi_")&&sessionStorage.removeItem(a)}catch(g){}},print:function(){for(var h=document.cookie.split(";"),b="",f=0;f<h.length;f++){var e=h[f];0==e.trim().toLowerCase().indexOf("usi_")&&(console.log(decodeURIComponent(e.trim())+" (cookie)"),b+=","+e.trim().toLowerCase().split("=")[0]+",")}try{if(null!=localStorage)for(var a in localStorage)0==a.indexOf("usi_")&&"string"==typeof localStorage[a]&& -1==b.indexOf(","+a+",")&&(console.log(a+"="+usi_cookies.get_ls(a)+" (localStorage)"),b+=","+a+",");if(null!=sessionStorage)for(var a in sessionStorage)0==a.indexOf("usi_")&&"string"==typeof sessionStorage[a]&& -1==b.indexOf(","+a+",")&&(console.log(a+"="+sessionStorage[a]+" (sessionStorage)"),b+=","+a+",")}catch(j){}for(var i=(window.top||window).name.split(";"),g=0;g<i.length;g++){var d=i[g].split("=");if(3==d.length&&0==d[0].indexOf("usi_")&& -1==b.indexOf(","+d[0]+",")){var c=d[1];-1!=c.indexOf("USIEQLS")&&(c=c.replace(/USIEQLS/g,"=")),-1!=c.indexOf("USIPRNS")&&(c=c.replace(/USIPRNS/g,";")),console.log(d[0]+"="+c+" (window.name)"),b+=","+e.trim().toLowerCase().split("=")[0]+","}}},value_exists:function(){var b,a;for(b=0;b<arguments.length;b++)if(a=usi_cookies.get(arguments[b]),""===a||null===a||"null"===a||"undefined"===a)return!1;return!0},report_error:function(a){"undefined"!=typeof usi_commons&&"function"==typeof usi_commons.report_error&&usi_commons.report_error(a)}},"undefined"!=typeof usi_commons&&"function"==typeof usi_commons.gup&&"function"==typeof usi_commons.gup_or_get_cookie))try{""!=usi_commons.gup("usi_email_id")&&usi_cookies.set("usi_email_id",usi_commons.gup("usi_email_id").split(".")[0],Number(usi_commons.gup("usi_email_id").split(".")[1]),!0),""!=usi_commons.gup_or_get_cookie("usi_debug")&&(usi_commons.debug=!0),""!=usi_commons.gup_or_get_cookie("usi_qa")&&(usi_commons.domain=usi_commons.cdn="https://prod.upsellit.com")}catch(a){usi_commons.report_error(a)}
"undefined"==typeof usi_dom&&(usi_dom={},usi_dom.get_elements=function(e,t){return t=t||document,Array.prototype.slice.call(t.querySelectorAll(e))},usi_dom.count_elements=function(e,t){return t=t||document,usi_dom.get_elements(e,t).length},usi_dom.get_nth_element=function(e,t,n){var o=null;n=n||document;var r=usi_dom.get_elements(t,n);return r.length>=e&&(o=r[e-1]),o},usi_dom.get_first_element=function(e,t){if(""===(e||""))return null;if(t=t||document,"[object Array]"===Object.prototype.toString.call(e)){for(var n=null,o=0;o<e.length;o++){var r=e[o];if(null!=(n=usi_dom.get_first_element(r,t)))break}return n}return t.querySelector(e)},usi_dom.get_element_text_no_children=function(e,t){var n="";if(null==t&&(t=!1),null!=(e=e||document)&&null!=e.childNodes)for(var o=0;o<e.childNodes.length;++o)3===e.childNodes[o].nodeType&&(n+=e.childNodes[o].textContent);return!0===t&&(n=usi_dom.clean_string(n)),n.trim()},usi_dom.clean_string=function(e){if("string"==typeof e){return(e=(e=(e=(e=(e=(e=(e=e.replace(/[\u2010-\u2015\u2043]/g,"-")).replace(/[\u2018-\u201B]/g,"'")).replace(/[\u201C-\u201F]/g,'"')).replace(/\u2024/g,".")).replace(/\u2025/g,"..")).replace(/\u2026/g,"...")).replace(/\u2044/g,"/")).replace(/[^\x20-\xFF\u0100-\u017F\u0180-\u024F\u20A0-\u20CF]/g,"").trim()}},usi_dom.encode=function(e){if("string"==typeof e){var t=encodeURIComponent(e);return t=t.replace(/[-_.!~*'()]/g,function(e){return"%"+e.charCodeAt(0).toString(16).toUpperCase()})}},usi_dom.get_closest=function(e,t){for(e=e||document,"function"!=typeof Element.prototype.matches&&(Element.prototype.matches=Element.prototype.matchesSelector||Element.prototype.mozMatchesSelector||Element.prototype.msMatchesSelector||Element.prototype.oMatchesSelector||Element.prototype.webkitMatchesSelector||function(e){for(var t=(this.document||this.ownerDocument).querySelectorAll(e),n=t.length;--n>=0&&t.item(n)!==this;);return n>-1});null!=e&&e!==document;e=e.parentNode)if(e.matches(t))return e;return null},usi_dom.get_classes=function(e){var t=[];return null!=e&&null!=e.classList&&(t=Array.prototype.slice.call(e.classList)),t},usi_dom.add_class=function(e,t){if(null!=e){var n=usi_dom.get_classes(e);-1===n.indexOf(t)&&(n.push(t),e.className=n.join(" "))}},usi_dom.string_to_decimal=function(e){var t=null;if("string"==typeof e)try{var n=parseFloat(e.replace(/[^0-9\.-]+/g,""));!1===isNaN(n)&&(t=n)}catch(e){usi_commons.log("Error: "+e.message)}return t},usi_dom.string_to_integer=function(e){var t=null;if("string"==typeof e)try{var n=parseInt(e.replace(/[^0-9-]+/g,""));!1===isNaN(n)&&(t=n)}catch(e){usi_commons.log("Error: "+e.message)}return t},usi_dom.get_currency_string_from_content=function(e){if("string"!=typeof e)return"";try{e=e.trim();var t=e.match(/^([^\$]*?)(\$(?:[\,\,]?\d{1,3})+(?:\.\d{2})?)(.*?)$/)||[];return 4===t.length?t[2]:""}catch(e){return usi_commons.log("Error: "+e.message),""}},usi_dom.get_absolute_url=function(){var e;return function(t){return(e=e||document.createElement("a")).href=t,e.href}}(),usi_dom.format_number=function(e,t){var n="";if("number"==typeof e){t=t||0;var o=e.toFixed(t).split(/\./g);if(1==o.length||2==o.length)n=o[0].replace(/./g,function(e,t,n){return t&&"."!==e&&(n.length-t)%3==0?","+e:e}),2==o.length&&(n+="."+o[1])}return n},usi_dom.format_currency=function(e,t,n){var o="";return e=Number(e),!1===isNaN(e)&&("object"==typeof Intl&&"function"==typeof Intl.NumberFormat?(t=t||"en-US",n=n||{style:"currency",currency:"USD"},o=e.toLocaleString(t,n)):o=e),o},usi_dom.to_decimal_places=function(e,t){if(null!=e&&"number"==typeof e&&null!=t&&"number"==typeof t){if(0==t)return parseFloat(Math.round(e));for(var n=10,o=1;o<t;o++)n*=10;return parseFloat(Math.round(e*n)/n)}return null},usi_dom.trim_string=function(e,t,n){return n=n||"",(e=e||"").length>t&&(e=e.substring(0,t),""!==n&&(e+=n)),e},usi_dom.attach_event=function(e,t,n){var o=usi_dom.find_supported_element(e,n);usi_dom.detach_event(e,t,o),o.addEventListener?o.addEventListener(e,t,!1):o.attachEvent("on"+e,t)},usi_dom.detach_event=function(e,t,n){var o=usi_dom.find_supported_element(e,n);o.removeEventListener?o.removeEventListener(e,t,!1):o.detachEvent("on"+e,t)},usi_dom.find_supported_element=function(e,t){return(t=t||document)===window?window:!0===usi_dom.is_event_supported(e,t)?t:t===document?window:usi_dom.find_supported_element(e,document)},usi_dom.is_event_supported=function(e,t){return null!=t&&void 0!==t["on"+e]},usi_dom.is_defined=function(e,t){if(null==e)return!1;if(""===(t||""))return!1;var n=!0,o=e;return t.split(".").forEach(function(e){!0===n&&(null==o||"object"!=typeof o||!1===o.hasOwnProperty(e)?n=!1:o=o[e])}),n},usi_dom.observe=function(e,t,n){var o=location.href,r=window.MutationObserver||window.WebkitMutationObserver;return t=t||{onUrlUpdate:!1,observerOptions:{childList:!0,subtree:!0}},function(e,n){var i=null,u=function(){var e=location.href;t.onUrlUpdate&&e!==o?(n(),o=e):n()};return r?(i=new r(function(e){var r=location.href,i=e[0].addedNodes.length||e[0].removedNodes.length;i&&t.onUrlUpdate&&r!==o?(n(),o=r):i&&n()})).observe(e,t.observerOptions):window.addEventListener&&(e.addEventListener("DOMNodeInserted",u,!1),e.addEventListener("DOMNodeRemoved",u,!1)),i}}(),usi_dom.params_to_object=function(e){var t={};""!=(e||"")&&e.split("&").forEach(function(e){var n=e.split("=");2===n.length?t[decodeURIComponent(n[0])]=decodeURIComponent(n[1]):1===n.length&&(t[decodeURIComponent(n[0])]=null)});return t},usi_dom.object_to_params=function(e){var t=[];if(null!=e)for(var n in e)!0===e.hasOwnProperty(n)&&t.push(encodeURIComponent(n)+"="+(null==e[n]?"":encodeURIComponent(e[n])));return t.join("&")},usi_dom.interval_with_timeout=function(e,t,n,o){if("function"!=typeof e)throw new Error("usi_dom.interval_with_timeout(): iterationFunction must be a function");if(null==t)t=function(e){return e};else if("function"!=typeof t)throw new Error("usi_dom.interval_with_timeout(): timeoutCallback must be a function");if(null==n)n=function(e){return e};else if("function"!=typeof n)throw new Error("usi_dom.interval_with_timeout(): completeCallback must be a function");var r=(o=o||{}).intervalMS||20,i=o.timeoutMS||2e3;if("number"!=typeof r)throw new Error("usi_dom.interval_with_timeout(): intervalMS must be a number");if("number"!=typeof i)throw new Error("usi_dom.interval_with_timeout(): timeoutMS must be a number");var u=!1,l=new Date,a=setInterval(function(){var o=new Date-l;if(o>=i)return clearInterval(a),t({elapsedMS:o});!1===u&&(u=!0,e(function(e,t){if(u=!1,!0===e)return clearInterval(a),(t=t||{}).elapsedMS=new Date-l,n(t)}))},r)},usi_dom.load_external_stylesheet=function(e,t,n){if(""!==(e||"")){""===(t||"")&&(t="usi_stylesheet_"+(new Date).getTime());var o={url:e,id:t},r=document.getElementsByTagName("head")[0];if(null!=r){var i=document.createElement("link");i.type="text/css",i.rel="stylesheet",i.id=o.id,i.href=e,usi_dom.attach_event("load",function(){if(null!=n)return n(null,o)},i),r.appendChild(i)}}else if(null!=n)return n(null,o)},usi_dom.ready=function(e){void 0!==document.readyState&&"complete"===document.readyState?e():window.addEventListener?window.addEventListener("load",e,!0):window.attachEvent?window.attachEvent("onload",e):setTimeout(e,5e3)},usi_dom.fit_text=function(e,t){t||(t={});var n={multiLine:!0,minFontSize:.1,maxFontSize:20,widthOnly:!1},o={};for(var r in n)t.hasOwnProperty(r)?o[r]=t[r]:o[r]=n[r];var i=Object.prototype.toString.call(e);function u(e,t){var n,o,r,i,u,l,a,s;r=e.innerHTML,u=parseInt(window.getComputedStyle(e,null).getPropertyValue("font-size"),10),i=function(e){var t=window.getComputedStyle(e,null);return(e.clientWidth-parseInt(t.getPropertyValue("padding-left"),10)-parseInt(t.getPropertyValue("padding-right"),10))/u}(e),o=function(e){var t=window.getComputedStyle(e,null);return(e.clientHeight-parseInt(t.getPropertyValue("padding-top"),10)-parseInt(t.getPropertyValue("padding-bottom"),10))/u}(e),i&&(t.widthOnly||o)||(t.widthOnly?usi_commons.log("Set a static width on the target element "+e.outerHTML):usi_commons.log("Set a static height and width on the target element "+e.outerHTML)),-1===r.indexOf("textFitted")?((n=document.createElement("span")).className="textFitted",n.style.display="inline-block",n.innerHTML=r,e.innerHTML="",e.appendChild(n)):n=e.querySelector("span.textFitted"),t.multiLine||(e.style["white-space"]="nowrap"),l=t.minFontSize,s=t.maxFontSize;for(var c=l,d=1e3;l<=s&&d>0;)d--,a=s+l-.1,n.style.fontSize=a+"em",n.scrollWidth/u<=i&&(t.widthOnly||n.scrollHeight/u<=o)?(c=a,l=a+.1):s=a-.1;n.style.fontSize!==c+"em"&&(n.style.fontSize=c+"em")}"[object Array]"!==i&&"[object NodeList]"!==i&&"[object HTMLCollection]"!==i&&(e=[e]);for(var l=0;l<e.length;l++)u(e[l],o)});
'undefined'==typeof usi_url&&(usi_url={},usi_url.URL=function(a){a=a||location.href;var b=document.createElement('a');if(b.href=a,this.full=b.href||'',this.protocol=(b.protocol||'').split(':')[0],this.host=b.host||'',-1!=this.host.indexOf(':')&&(this.host=this.host.substring(0,this.host.indexOf(':'))),this.port=b.port||'',this.hash=b.hash||'',this.baseURL='',this.tld='',this.domain='',this.subdomain='',this.domain_tld='',''!==this.protocol&&''!==this.host){this.baseURL=this.protocol+'://'+this.host+'/';var c=this.host.split(/\./g);if(2<=c.length){if(-1<['co','com','org','net','int','edu','gov','mil'].indexOf(c[c.length-2])&&2===c[c.length-1].length){var d=c.pop(),e=c.pop();this.tld=e+'.'+d}else this.tld=c.pop()}0<c.length&&(this.domain=c.pop(),0<c.length&&(this.subdomain=c.join('.'))),this.domain_tld=this.domain+'.'+this.tld}var f=b.pathname||'';0!==f.indexOf('/')&&(f='/'+f),this.path=new usi_url.Path(f),this.params=new usi_url.Params((b.search||'').substr(1))},usi_url.URL.prototype.build=function(a,b,c){var d='';return''!==this.protocol&&''!==this.host&&(null==a&&(a=!0),null==b&&(b=!0),null==c&&(c=!0),!0==a&&(d+=this.protocol+':'),d+='//'+this.host,''!==this.port&&(d+=':'+this.port),!0==b&&(d+=this.path.full,!0==c&&0<Object.keys(this.params.parameters).length&&(d+='?',d+=this.params.build()))),d},usi_url.Path=function(a){a=a||'',this.full=a,this.directories=[],this.filename='';for(var b=a.substr(1).split(/\//g);0<b.length;)1===b.length?this.filename=b.shift():this.directories.push(b.shift());this.has_directory=function(a){return-1<this.directories.indexOf(a)},this.contains=function(a){return-1<this.full.indexOf(a)}},usi_url.Params=function(a){a=a||'',this.full=a,this.parameters=function(a){var b={};if(1===a.length&&''===a[0])return b;for(var c,d,e,f=0;f<a.length;f++)if(e=a[f].split('='),c=e[0]&&e[0].replace(/\+/g,' '),d=e[1]&&e[1].replace(/\+/g,' '),1===e.length)b[c]='';else try{b[c]=decodeURIComponent(d)}catch(a){b[c]=d}return b}(a.split('&')),this.count=Object.keys(this.parameters).length,this.get=function(a){return a in this.parameters?this.parameters[a]:null},this.has=function(a){return a in this.parameters},this.set=function(a,b){this.parameters[a]=b,this.count=Object.keys(this.parameters).length},this.remove=function(a){!0===this.has(a)&&delete this.parameters[a],this.count=Object.keys(this.parameters).length},this.build=function(){var a=this,b=[];for(var c in a.parameters)!0===a.parameters.hasOwnProperty(c)&&b.push(c+'='+encodeURIComponent(a.parameters[c]));return b.join('&')},this.remove_usi_params=function(a){var b=this;for(var c in a=a||[],-1===a.indexOf('usi_')&&a.push('usi_'),b.parameters)if(!0===b.parameters.hasOwnProperty(c)){var d=!1;a.forEach(function(a){0===c.indexOf(a)&&(d=!0)}),d&&b.remove(c)}},this.remove_all=function(){var a=this;for(var b in a.parameters)!0===a.parameters.hasOwnProperty(b)&&a.remove(b)}});

		usi_cookieless = true;
		usi_app = {};
		usi_app.main = function () {
			try {
				// General
				usi_app.url = new usi_url.URL(location.href.toLowerCase());

				usi_app.coupon = usi_cookies.value_exists("usi_coupon_applied") ? "" : usi_commons.gup_or_get_cookie("usi_coupon", usi_cookies.expire_time.week, true);

				// Pages
				usi_app.is_checkout_page = usi_app.url.path.full === "/cart/checkout/";
				usi_app.is_cart_page = usi_app.url.path.full === "/cart/";
				usi_app.is_login_page = usi_app.url.path.contains("/join/login-popup/");
				usi_app.is_promo_page = usi_app.url.path.contains("/gift-promo-code/redeem/");
				usi_app.is_confirmation_page = usi_app.url.path.contains("/cart/success/");

				// Booleans
				usi_app.is_enabled = usi_commons.gup_or_get_cookie("usi_enable", usi_cookies.expire_time.day, true) != "";
				usi_app.is_suppressed = usi_app.is_confirmation_page;

				if (location.href.toLowerCase().indexOf("utm_source=aff-campaign") != -1) {
					usi_cookies.set("usi_aff", "1", usi_cookies.expire_time.month, true);
				}
				usi_app.is_affiliate_traffic = usi_cookies.value_exists("usi_aff");

				// Load pixel on confirmation page
				if (usi_app.is_confirmation_page && typeof USI_orderID == "undefined") {
					usi_commons.load_script("//www.upsellit.com/active/udemy_pixel.jsp");
				}

				// Apply coupon
				if (usi_app.coupon !== "") {
					if (usi_app.is_login_page) {
						usi_app.boostbar.load("Please log in to redeem coupon");
						return;
					} else if (usi_app.is_promo_page) {
						usi_app.apply_coupon();
						return;
					}
				}

				// Check suppressions
				if (usi_app.is_suppressed) {
					return usi_commons.log("[ main ] Company is suppressed");
				}

				// Save cart data
				if (usi_app.is_cart_page) {
					usi_app.save_cart();
				}

				// Load campaigns
				usi_app.load();
			} catch (err) {
				usi_commons.report_error(err);
			}
		};

		usi_app.load = function () {
			try {
				// Clean up previous solutions
				if (typeof usi_js !== 'undefined' && typeof usi_js.cleanup === 'function') {
					usi_js.cleanup();
				}

				if (usi_app.is_affiliate_traffic && (usi_app.is_cart_page || usi_app.is_checkout_page) && usi_cookies.value_exists("usi_prod_image_1", "usi_prod_name_1", "usi_prod_price_1", "usi_prod_original_price_1")) {
					if ("US,CA,AU".indexOf(usi_app.country.toUpperCase()) != -1) {
						usi_commons.load_view("XvQnu7VvZqft6PL5kl3XtSi", "38251", usi_commons.device);
					} else if ("GB".indexOf(usi_app.country.toUpperCase()) != -1) {
						usi_commons.load_view("y2K1Da7x4aewPDh4zPnEZPI", "41970", usi_commons.device);
					} else if ("DE".indexOf(usi_app.country.toUpperCase()) != -1) {
						usi_commons.load_view("5mvRANxcmAtSMVO2eQEGbet", "41972", usi_commons.device);
					}
				}
			} catch(err) {
				usi_commons.report_error(err);
			}
		};

		usi_app.save_cart = function () {
			try {
				var prod_prefix = "usi_prod_";
				usi_cookies.flush(prod_prefix);
				usi_cookies.del("usi_subtotal");

				// Scrape cart
				usi_app.cart = {
					items: usi_app.scrape_cart(),
					subtotal: usi_app.scrape_subtotal()
				}

				// Save cart items
				if (typeof usi_app.cart.items != "undefined") {
					usi_app.cart.items.forEach(function (product, index) {
						var prop;
						if (index >= 1) return;
						for (prop in product) {
							if (product.hasOwnProperty(prop)) {
								usi_cookies.set(prod_prefix + prop + "_" + (index + 1), encodeURIComponent(product[prop]), usi_cookies.expire_time.week);
							}
						}
					});
				}

				usi_commons.log('[ save_cart ] cart:', usi_app.cart);
			} catch (err) {
				usi_commons.report_error(err);
			}
		};

		usi_app.scrape_subtotal = function () {
			try {
				var subtotal = document.querySelector("div[data-purpose='total-price'] .course-price-text span span");
				if (subtotal != null) {
					subtotal = usi_dom.string_to_decimal(subtotal.textContent).toFixed(2);
					usi_cookies.set("usi_subtotal", encodeURIComponent(subtotal), usi_cookies.expire_time.week);
					return subtotal;
				}
			} catch (err) {
				usi_commons.report_error(err);
			}
		};

		usi_app.scrape_cart = function () {
			try {
				var items = [], product;
				if (window['localStorage'] && window['localStorage']['shoppingCartStorage:storage-1.0']) {
					var cart_data = JSON.parse(window['localStorage']['shoppingCartStorage:storage-1.0']);
					if (cart_data['state'] && cart_data['state']['lists'] && cart_data['state']['lists']['cart']) {
						var cart_rows = cart_data['state']['lists']['cart'];
						cart_rows.forEach(function (item) {
							usi_commons.log('[ scrape_cart ] item:', item);
							var buyable = item['buyable'];
							if (buyable && item['purchase_price'] && item['list_price']) {
								product = {};
								product.pid = buyable['id'];
								product.name = buyable['title'];
								product.price = item['purchase_price']['amount'];
								product.original_price = item['list_price']['amount'];
								product.image = buyable['image_480x270'] || buyable['image_240x135'] || buyable['image_125_H'] || buyable['image_100x100'];
								
								items.push(product);
							}
						});
					}
				}
				return items;
			} catch (err) {
				usi_commons.report_error(err);
			}
		};

		usi_app.boostbar = {
			load: function (boost_txt) {
				try {
					if (boost_txt.length > 0 && !document.getElementById('usi_boost_container')) {
						// Assign boost bar styles according to condition
						var bg_color = "#EC5252";
						var close_right = "0";
						var padding = "1.1em 0";
						var usi_boost_container = document.createElement('div');
						var close_button = '<a href="javascript:usi_app.boostbar.close();" style="min-width: 50px; height:100%; width:20px; right:' + close_right + '; top:0; bottom:0; position:absolute; color:#fff !important; font-size:1.5em; text-decoration:none; line-height:1.5em">&times;</a>';
						usi_boost_container.innerHTML = [
							'<div id="usi_boost_container" style="position:fixed; bottom:0; left:0; width:100%; text-align:center; font-size:1.2em; background:' + bg_color + '; color:#fff; padding:' + padding + '; line-height: 1.2em; z-index:99999999999;">',
							close_button,
							'<p style="color: white !important; margin: 0 20%;">' + boost_txt + '</p>',
							'</div>'
						].join('');
						document.body.appendChild(usi_boost_container);
					}
				} catch (err) {
					usi_commons.report_error(err);
				}
			},
			close: function () {
				try {
					var bar = document.getElementById('usi_boost_container');
					if (bar != null) {
						usi_cookies.set('usi_suppress_boost', '1', usi_cookies.expire_time.day);
						bar.parentNode.removeChild(bar);
					}
				} catch (err) {
					usi_commons.report_error(err);
				}
			}
		};

		usi_app.apply_coupon = function () {
			try {
				var coupon_input = document.querySelector("#formBasicWithHelpBlockText");
				var coupon_button = document.querySelector("button[data-purpose='redeem-code-button']");
				if (coupon_input !== null && coupon_button !== null) {
					var customEvent = new Event('input', {bubbles: true});
					var lastValue = coupon_input.value;
					customEvent.simulated = true;
					coupon_input.value = usi_app.coupon;
					coupon_input.defaultValue = usi_app.coupon;
					var tracker = coupon_input._valueTracker;
					if (tracker) {
						tracker.setValue(lastValue);
					}
					coupon_input.dispatchEvent(customEvent);
					usi_cookies.set("usi_coupon_applied", usi_app.coupon, usi_cookies.expire_time.week);
					usi_cookies.del("usi_coupon");
					usi_app.coupon = "";
					coupon_button.click();
					setTimeout(usi_app.post_apply_coupon, 2000);
					usi_commons.log("[ apply_coupon ] Coupon applied");
				} else {
					if (usi_app.coupon_attempts == undefined) {
						usi_app.coupon_attempts = 0;
					} else if (usi_app.coupon_attempts >= 5) {
						usi_commons.report_error("[ apply_coupon ] Coupon elements not found");
						return;
					}
					usi_app.coupon_attempts++;
					usi_commons.log("[ apply_coupon ] Coupon elements missing, trying again. Tries: " + usi_app.coupon_attempts);
					setTimeout(usi_app.apply_coupon, 1000);
				}
			} catch (err) {
				usi_commons.report_error(err);
			}
		};

		usi_app.post_apply_coupon = function () {
			try {
				var error_element = document.querySelector(".help-block div[data-purpose='safely-set-inner-html:form:error']");
				var error_message_exists = error_element != null && error_element.textContent.trim() != "";
				if (error_message_exists) {
					usi_commons.report_error("[ post_apply_coupon ] Coupon error message seen");
				} else {
					usi_commons.log_success("[ post_apply_coupon ] Coupon application was successful");
				}
			} catch (err) {
				usi_commons.report_error(err);
			}
		};

		usi_app.session_data_callback = function() {
			usi_app.country = usi_app.session_data.country;
			usi_app.main();
		};
		usi_dom.ready(function () {
			try {
				usi_commons.load_session_data();
			} catch (err) {
				usi_commons.report_error(err);
			}
		});

	} catch (err) {
		usi_commons.report_error(err);
	}
}
