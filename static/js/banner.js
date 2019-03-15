/**
 * Created by Administrator on 2018/1/10.
 * form by 好好好先生
 * email 1570302023@qq.com
 *
 *
 *
 */

$(function(){
    // $('.bot-img ul li').click(function(){
    //     var _this=$(this);
    //     _this.addClass('active').siblings('li').removeClass('active');
    //     var int=_this.index();
    //     $('.activeimg').animate({left:int*-847.5},"slow");
    // });
    var list=$('.activeimg img').length;
    $('.activeimg').css({
        width:list*847,
    });
    $('.right').click(function(){
        next(list)

    })
    $('.left').click(function(){
        prev(list)
    });

    //自动播放 2秒播放一次 无限循环
    var timer='';
    var num=0;
    timer=setInterval(function(){ //打开定时器
        num++;
        if(num>parseFloat(list)-1){
            num=0;
            $('.activeimg').animate({left:num*-847},"slow");
        }else{
            $('.activeimg').animate({left:num*-847},"slow");
        }
    },3000);
})
var index=0;
//下一张
function next(list){
    if(index<list-1){
        index++;
        $('.activeimg').animate({left:index*-847},"slow");
        $('.bot-img ul li').eq(index).addClass('active').siblings('li').removeClass('active')
    }else{
        index=0;
        $('.activeimg').animate({left:index*-847},"slow");
        $('.bot-img ul li').eq(index).addClass('active').siblings('li').removeClass('active')
    }
}
//        上一张
function prev(list){
    index--;
    if(index<0){
        index=list-1;
        $('.activeimg').animate({left:index*-847},"slow");
        $('.bot-img ul li').eq(index).addClass('active').siblings('li').removeClass('active')
    }else{
        $('.activeimg').animate({left:index*-847},"slow");
        $('.bot-img ul li').eq(index).addClass('active').siblings('li').removeClass('active')
    }
}


