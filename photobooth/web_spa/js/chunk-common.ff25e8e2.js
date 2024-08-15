"use strict";(globalThis["webpackChunkphotobooth_app_frontend"]=globalThis["webpackChunkphotobooth_app_frontend"]||[]).push([[64],{9523:(e,i,t)=>{t.d(i,{Z:()=>K});t(72879);var l=t(59835),r=t(86970);const s={class:"q-ml-sm"},n={class:"q-ml-sm"},a={key:5,class:"q-mr-sm"},o={class:"q-mr-sm"},d={class:"text-subtitle2"},c={key:0,class:"full-height"},m={key:0,class:"full-height"},u=["src"],g={key:1,class:"full-height"},p=["src"],h={key:1,class:"full-height"},y={key:0,class:"full-height"},w=["src"],f={key:1,class:"full-height"},I=["src"];function S(e,i,t,S,_,b){const v=(0,l.up)("q-btn"),q=(0,l.up)("q-space"),k=(0,l.up)("q-avatar"),R=(0,l.up)("q-card-section"),L=(0,l.up)("q-card-actions"),x=(0,l.up)("q-card"),E=(0,l.up)("q-dialog"),T=(0,l.up)("q-icon"),D=(0,l.up)("q-toolbar"),A=(0,l.up)("q-linear-progress"),F=(0,l.up)("q-header"),C=(0,l.up)("q-img"),W=(0,l.up)("q-drawer"),$=(0,l.up)("q-carousel-slide"),B=(0,l.up)("q-carousel"),N=(0,l.up)("vue-qrcode"),Z=(0,l.up)("q-page-sticky"),Q=(0,l.up)("q-page-container"),V=(0,l.up)("q-layout"),j=(0,l.Q2)("close-popup"),O=(0,l.Q2)("touch-swipe");return b.emptyRepository?((0,l.wg)(),(0,l.j4)(V,{key:1,view:"hhh Lpr ffr"},{default:(0,l.w5)((()=>[(0,l.Uk)("EMPTY")])),_:1})):((0,l.wg)(),(0,l.j4)(V,{key:0,view:"hhh Lpr ffr",onClick:b.abortTimer},{default:(0,l.w5)((()=>[(0,l.Wm)(F,{elevated:"",class:"bg-primary text-white"},{default:(0,l.w5)((()=>[t.showToolbar?((0,l.wg)(),(0,l.j4)(D,{key:0,class:"toolbar",id:"gallery-toolbar"},{default:(0,l.w5)((()=>[(0,l.Wm)(v,{dense:"",flat:"",icon:"close",size:"1.5rem",onClick:i[0]||(i[0]=i=>e.$emit("closeEvent"))}),(0,l.Wm)(q),S.uiSettingsStore.uiSettings.gallery_show_delete||t.singleItemView?((0,l.wg)(),(0,l.j4)(v,{key:0,flat:"",class:"q-mr-sm",icon:"delete",label:e.$t("BTN_LABEL_GALLERY_DELETE"),onClick:i[1]||(i[1]=e=>S.confirmDeleteFile=!0)},null,8,["label"])):(0,l.kq)("",!0),(0,l.Wm)(E,{modelValue:S.confirmDeleteFile,"onUpdate:modelValue":i[3]||(i[3]=e=>S.confirmDeleteFile=e)},{default:(0,l.w5)((()=>[(0,l.Wm)(x,{class:"q-pa-sm",style:{"min-width":"350px"},id:"gallery-confirm-delete-dialog"},{default:(0,l.w5)((()=>[(0,l.Wm)(R,{class:"row items-center"},{default:(0,l.w5)((()=>[(0,l.Wm)(k,{icon:"delete",color:"primary","text-color":"white"}),(0,l._)("span",s,(0,r.zw)(e.$t("MSG_CONFIRM_DELETE_IMAGE")),1)])),_:1}),(0,l.Wm)(L,{align:"right"},{default:(0,l.w5)((()=>[(0,l.wy)((0,l.Wm)(v,{flat:"",label:e.$t("BTN_LABEL_CANCEL")},null,8,["label"]),[[j]]),(0,l.wy)((0,l.Wm)(v,{label:e.$t("BTN_LABEL_DELETE_IMAGE"),color:"primary",onClick:i[2]||(i[2]=i=>{b.deleteItem(S.currentSlideId),e.$emit("closeEvent")})},null,8,["label"]),[[j]])])),_:1})])),_:1})])),_:1},8,["modelValue"]),S.uiSettingsStore.uiSettings.gallery_show_download?((0,l.wg)(),(0,l.j4)(v,{key:1,flat:"",class:"q-mr-sm",icon:"download",label:e.$t("BTN_LABEL_GALLERY_DOWNLOAD"),onClick:i[4]||(i[4]=e=>{S.openURL(t.itemRepository[S.currentSlideIndex]["full"])})},null,8,["label"])):(0,l.kq)("",!0),S.uiSettingsStore.uiSettings.gallery_show_print&&t.singleItemView&&("image"==this.itemRepository[0].media_type||"collage"==this.itemRepository[0].media_type)?((0,l.wg)(),(0,l.j4)(v,{key:2,flat:"",class:"q-mr-sm",icon:"print",label:e.$t("BTN_LABEL_GALLERY_PRINT"),onClick:i[5]||(i[5]=e=>S.confirmPrintSingle=!0)},null,8,["label"])):(0,l.kq)("",!0),(0,l.Wm)(E,{modelValue:S.confirmPrintSingle,"onUpdate:modelValue":i[7]||(i[7]=e=>S.confirmPrintSingle=e)},{default:(0,l.w5)((()=>[(0,l.Wm)(x,{class:"q-pa-sm",style:{"min-width":"350px"},id:"gallery-confirm-print-dialog"},{default:(0,l.w5)((()=>[(0,l.Wm)(R,{class:"row items-center"},{default:(0,l.w5)((()=>[(0,l.Wm)(k,{icon:"delete",color:"primary","text-color":"white"}),(0,l._)("span",n,(0,r.zw)(e.$t("MSG_CONFIRM_PRINT_IMAGE")),1)])),_:1}),(0,l.Wm)(L,{align:"right"},{default:(0,l.w5)((()=>[(0,l.wy)((0,l.Wm)(v,{flat:"",label:e.$t("BTN_LABEL_CANCEL")},null,8,["label"]),[[j]]),(0,l.wy)((0,l.Wm)(v,{label:e.$t("BTN_LABEL_PRINT_IMAGE"),color:"primary",onClick:i[6]||(i[6]=i=>{b.printItem(S.currentSlideId),e.$emit("closeEvent")})},null,8,["label"]),[[j]])])),_:1})])),_:1})])),_:1},8,["modelValue"]),!S.uiSettingsStore.uiSettings.gallery_show_print||t.singleItemView||"image"!=this.itemRepository[S.currentSlideIndex].media_type&&"collage"!=this.itemRepository[S.currentSlideIndex].media_type?(0,l.kq)("",!0):((0,l.wg)(),(0,l.j4)(v,{key:3,flat:"",class:"q-mr-sm",icon:"print",label:e.$t("BTN_LABEL_GALLERY_PRINT"),to:`/gallery/print/${S.currentSlideIndex}`},null,8,["label","to"])),S.uiSettingsStore.uiSettings.gallery_show_filter&&S.uiSettingsStore.uiSettings.gallery_filter_userselectable.length>0?((0,l.wg)(),(0,l.j4)(v,{key:4,flat:"",class:"q-mr-sm",icon:"filter",label:e.$t("BTN_LABEL_GALLERY_FILTER"),disabled:!b.getFilterAvailable(t.itemRepository[S.currentSlideIndex]["media_type"]),onClick:S.toggleRightDrawer},null,8,["label","disabled","onClick"])):(0,l.kq)("",!0),(0,l.Wm)(q),t.singleItemView?(0,l.kq)("",!0):((0,l.wg)(),(0,l.iD)("div",a,[(0,l.Wm)(T,{name:"tag"}),(0,l._)("span",null,(0,r.zw)(S.currentSlideIndex+1)+" / "+(0,r.zw)(t.itemRepository.length),1)])),(0,l.Wm)(q),(0,l._)("div",o,[(0,l.Wm)(T,{name:"image"}),(0,l.Uk)(" "+(0,r.zw)(t.itemRepository[S.currentSlideIndex]["caption"]),1)])])),_:1})):(0,l.kq)("",!0),_.displayLinearProgressBar&&_.remainingSeconds>0?((0,l.wg)(),(0,l.j4)(A,{key:1,class:"absolute",value:_.remainingSecondsNormalized,"animation-speed":"200",color:"grey",id:"gallery-linear-progress-bar"},null,8,["value"])):(0,l.kq)("",!0),S.displayLoadingSpinner?((0,l.wg)(),(0,l.j4)(A,{key:2,class:"absolute",indeterminate:"","animation-speed":"2100",color:"primary"})):(0,l.kq)("",!0)])),_:1}),S.uiSettingsStore.uiSettings.gallery_show_filter&&b.getFilterAvailable(t.itemRepository[S.currentSlideIndex]["media_type"])&&t.showToolbar?((0,l.wg)(),(0,l.j4)(W,{key:0,class:"q-pa-sm",modelValue:S.rightDrawerOpen,"onUpdate:modelValue":i[8]||(i[8]=e=>S.rightDrawerOpen=e),side:"right",overlay:"",id:"gallery-drawer-filters"},{default:(0,l.w5)((()=>[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(S.uiSettingsStore.uiSettings.gallery_filter_userselectable,(e=>((0,l.wg)(),(0,l.j4)(x,{class:"q-mb-sm",key:e},{default:(0,l.w5)((()=>[(0,l.Wm)(R,{class:"q-pa-sm"},{default:(0,l.w5)((()=>[(0,l.Wm)(C,{class:"rounded-borders",loading:"lazy",onClick:i=>b.applyFilter(S.currentSlideId,e),src:`/mediaprocessing/preview/${S.currentSlideId}/${e}`},null,8,["onClick","src"])])),_:2},1024),(0,l.Wm)(R,{class:"q-pa-none q-pb-sm",align:"center"},{default:(0,l.w5)((()=>[(0,l._)("div",d,(0,r.zw)(e),1)])),_:2},1024)])),_:2},1024)))),128))])),_:1},8,["modelValue"])):(0,l.kq)("",!0),(0,l.Wm)(Q,{class:"q-pa-none galleryimagedetail full-height"},{default:(0,l.w5)((()=>[t.singleItemView?((0,l.wg)(),(0,l.iD)("div",c,[(0,l.Wm)(x,{class:"column no-wrap flex-center full-height q-pa-sm"},{default:(0,l.w5)((()=>["video"!=this.itemRepository[0].media_type?((0,l.wg)(),(0,l.iD)("div",m,[(0,l._)("img",{draggable:!1,class:"rounded-borders full-height",style:{"object-fit":"contain","max-width":"100%","max-height":"100%"},src:this.itemRepository[0].preview},null,8,u)])):((0,l.wg)(),(0,l.iD)("div",g,[(0,l._)("video",{draggable:!1,src:this.itemRepository[0].preview,class:"rounded-borders full-height",muted:"",autoplay:"",style:{"object-fit":"contain","max-width":"100%","max-height":"100%"},controls:"controls"},null,8,p)]))])),_:1})])):((0,l.wg)(),(0,l.iD)("div",h,[(0,l.wy)(((0,l.wg)(),(0,l.j4)(B,{class:"",style:{width:"100%",height:"100%"},"control-type":"flat","control-color":"primary",swipeable:"",animated:"",modelValue:S.currentSlideId,"onUpdate:modelValue":i[9]||(i[9]=e=>S.currentSlideId=e),autoplay:t.slideshowTimeout,draggable:"false",arrows:t.showToolbar,infinite:!0,"transition-prev":t.slideshowUseFade?"fade":"slide-right","transition-next":t.slideshowUseFade?"fade":"slide-left",onTransition:i[10]||(i[10]=(i,l)=>{if(t.randomOrder){let t=b.slicedImages.findIndex((e=>e.id==i));S.currentSlideIndex=e.rndIncides[t],t>2?e.rndIncidesFull.push(e.rndIncidesFull.shift()):e.rndIncidesFull.unshift(e.rndIncidesFull.pop()),e.rndIncides=e.rndIncidesFull.slice(0,5)}else S.currentSlideIndex=t.itemRepository.findIndex((e=>e.id===i));console.log("Showing slide ",S.currentSlideIndex),b.abortTimer()})},{default:(0,l.w5)((()=>[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(b.slicedImages,(e=>((0,l.wg)(),(0,l.j4)($,{key:e.id,name:e.id,class:"column no-wrap flex-center full-height q-pa-sm"},{default:(0,l.w5)((()=>["video"!=e.media_type?((0,l.wg)(),(0,l.iD)("div",y,[(0,l._)("img",{draggable:!1,class:"rounded-borders full-height",style:{"object-fit":"contain","max-width":"100%","max-height":"100%"},src:e.preview},null,8,w)])):((0,l.wg)(),(0,l.iD)("div",f,[(0,l._)("video",{draggable:!1,src:e.preview,class:"rounded-borders full-height",style:{"object-fit":"contain","max-width":"100%","max-height":"100%"},controls:"controls"},null,8,I)]))])),_:2},1032,["name"])))),128))])),_:1},8,["modelValue","autoplay","arrows","transition-prev","transition-next"])),[[O,S.handleSwipeDown,void 0,{mouse:!0,down:!0}]])])),S.uiSettingsStore.uiSettings.gallery_show_qrcode&&t.showToolbar?((0,l.wg)(),(0,l.j4)(Z,{key:2,position:"top-right",offset:[30,30]},{default:(0,l.w5)((()=>[(0,l._)("div",null,[(0,l.Wm)(N,{type:"image/png",tag:"svg",margin:2,width:200,"error-correction-level":"low",color:{dark:"#111111",light:"#EEEEEE"},value:b.getImageQrData()},null,8,["value"])])])),_:1})):(0,l.kq)("",!0)])),_:1})])),_:1},8,["onClick"]))}var _=t(44556),b=t(60499),v=t(96694),q=t(33752),k=t(19302);const R={props:{indexSelected:{type:Number,required:!0},itemRepository:{type:Array,required:!0},startTimerOnOpen:{type:Boolean,required:!1,default:!1},singleItemView:{type:Boolean,default:!1},showToolbar:{type:Boolean,default:!0},slideshowTimeout:{type:Number,default:0},slideshowUseFade:{type:Boolean,default:!1},randomOrder:{type:Boolean,default:!1}},computed:{emptyRepository(){return!this.itemRepository||0==this.itemRepository.length},slicedImages(){if(this.randomOrder)return this.currentSlideIndex,console.log(this.rndIncides.map((e=>this.itemRepository[e]))),this.rndIncides.map((e=>this.itemRepository[e]));var e=Math.max(0,this.currentSlideIndex-2),i=Math.max(0,this.currentSlideIndex+3);return console.log(this.itemRepository.slice(e,i)),this.itemRepository.slice(e,i)}},beforeCreate(){if(!this.emptyRepository){if(this.randomOrder){this.rndIncidesFull=Array.from(Array(this.itemRepository.length).keys());for(let e=this.rndIncidesFull.length-1;e>0;e--){let i=Math.floor(Math.random()*(e+1)),t=this.rndIncidesFull[e];this.rndIncidesFull[e]=this.rndIncidesFull[i],this.rndIncidesFull[i]=t}while(this.rndIncidesFull.length<5)this.rndIncidesFull.push(...this.rndIncidesFull);this.rndIncides=this.rndIncidesFull.slice(0,5),console.log("Initial random indices: ",this.rndIncides),this.currentSlideIndex=this.rndIncides[2]}else this.currentSlideIndex=this.indexSelected;console.log("currentSlideIndex:",this.currentSlideIndex),this.currentSlideId=this.itemRepository[this.currentSlideIndex].id}},data(){return{intervalTimerId:null,remainingSeconds:0,remainingSecondsNormalized:0,displayLinearProgressBar:!0}},setup(){const e=(0,v.R)(),i=(0,b.iH)(!1);(0,k.Z)();return{uiSettingsStore:e,openURL:q.Z,fabRight:(0,b.iH)(!1),currentSlideId:(0,b.iH)(""),currentSlideIndex:(0,b.iH)(0),autoplay:(0,b.iH)(!1),showFilterDialog:(0,b.iH)(!1),displayLoadingSpinner:(0,b.iH)(!1),confirmDeleteFile:(0,b.iH)(!1),confirmPrintSingle:(0,b.iH)(!1),rightDrawerOpen:i,toggleRightDrawer(){i.value=!i.value},handleSwipeDown({evt:e}){console.log("TODO: add method to close dialog programmatically")}}},components:{VueQrcode:_.ZP},mounted(){this.startTimerOnOpen&&this.startTimer()},beforeUnmount(){clearInterval(this.intervalTimerId)},methods:{async reloadImg(e){await fetch(e,{cache:"reload",mode:"no-cors"});const i=(new Date).getTime();document.body.querySelectorAll(`img[src*='${e}']`).forEach((t=>{t.src=e+"#"+i}))},applyFilter(e,i){this.displayLoadingSpinner=!0,this.$api.get(`/mediaprocessing/applyfilter/${e}/${i}`).then((i=>{const t=this.itemRepository.findIndex((i=>i.id===e));this.reloadImg(this.itemRepository[t].full),this.reloadImg(this.itemRepository[t].preview),this.reloadImg(this.itemRepository[t].thumbnail),this.displayLoadingSpinner=!1})).catch((e=>{console.log(e),this.displayLoadingSpinner=!1}))},deleteItem(e){this.$api.get("/mediacollection/delete",{params:{image_id:e}}).then((e=>{console.log(e)})).catch((e=>console.log(e)))},printItem(e){this.$api.get(`/print/item/${e}`).then((e=>{console.log(e),this.$q.notify({message:"Started printing...",type:"positive",spinner:!0})})).catch((e=>{e.response?(console.log(e.response),425==e.response.status?this.$q.notify({message:e.response.data["detail"],caption:"Print Service",type:"info"}):this.$q.notify({message:e.response.data["detail"],caption:"Print Service",type:"negative"})):e.request?console.error(e.request):console.error("Error",e.message)}))},getFilterAvailable(e){return["image","collageimage","animationimage"].includes(e)},getImageQrData(){return this.itemRepository[this.currentSlideIndex]["share_url"]},abortTimer(){clearInterval(this.intervalTimerId),this.remainingSeconds=0,this.remainingSecondsNormalized=0},startTimer(){var e=this.uiSettingsStore.uiSettings["AUTOCLOSE_NEW_ITEM_ARRIVED"];console.log(`starting newitemarrived timer, duration=${e}`),this.remainingSeconds=e,this.intervalTimerId=setInterval((()=>{this.remainingSecondsNormalized=this.remainingSeconds/e,this.remainingSeconds-=.05,this.remainingSeconds<=0&&(clearInterval(this.intervalTimerId),this.$router.push({path:"/"}))}),50)}}};var L=t(11639),x=t(20249),E=t(16602),T=t(51663),D=t(68879),A=t(90136),F=t(32074),C=t(44458),W=t(63190),$=t(61357),B=t(11821),N=t(22857),Z=t(8289),Q=t(10906),V=t(70335),j=t(12133),O=t(97052),P=t(41694),M=t(30627),U=t(62146),z=t(64871),H=t(69984),G=t.n(H);const Y=(0,L.Z)(R,[["render",S]]),K=Y;G()(R,"components",{QLayout:x.Z,QHeader:E.Z,QToolbar:T.Z,QBtn:D.Z,QSpace:A.Z,QDialog:F.Z,QCard:C.Z,QCardSection:W.Z,QAvatar:$.Z,QCardActions:B.Z,QIcon:N.Z,QLinearProgress:Z.Z,QDrawer:Q.Z,QImg:V.Z,QPageContainer:j.Z,QCarousel:O.Z,QCarouselSlide:P.Z,QPageSticky:M.Z}),G()(R,"directives",{ClosePopup:U.Z,TouchSwipe:z.Z})}}]);