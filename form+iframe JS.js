$("#uploadfile").on("load",function(){  //iframe里面有个方法是onload，当上传数据成功之后服务器返回数据时才会触发该事件
            var rst=JSON.parse(this.contentDocument.body.textContent);//拿到iframe里面的内容需要通过contentDocument才能拿到里面的dom对象
            if (rst.state){
                var url="/"+rst.data;
                        $('<img class="show-img" src="'+url+'">').appendTo("#imgs")
            }
        })