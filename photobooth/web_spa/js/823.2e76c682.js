"use strict";(globalThis["webpackChunkphotobooth_app_frontend"]=globalThis["webpackChunkphotobooth_app_frontend"]||[]).push([[823],{77917:(e,t,i)=>{i.r(t),i.d(t,{default:()=>q});var o=i(59835);const l=e=>((0,o.dD)("data-v-398add10"),e=e(),(0,o.Cn)(),e),n={key:0,class:"row justify-center q-gutter-sm"},a={key:0},d={key:1},s=l((()=>(0,o._)("div",{style:{"padding-bottom":"100%"}},null,-1))),r={class:"absolute-full"},c=["src"],m=["innerHTML"];function u(e,t,i,l,u,g){const p=(0,o.up)("q-img"),h=(0,o.up)("q-card"),w=(0,o.up)("q-intersection"),y=(0,o.up)("gallery-image-detail"),_=(0,o.up)("q-dialog"),I=(0,o.up)("q-page");return(0,o.wg)(),(0,o.j4)(I,{padding:""},{default:(0,o.w5)((()=>[g.isGalleryEmpty?((0,o.wg)(),(0,o.iD)("div",{key:1,innerHTML:l.uiSettingsStore.uiSettings.GALLERY_EMPTY_MSG},null,8,m)):((0,o.wg)(),(0,o.iD)("div",n,[((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(this.mediacollectionStore.collection,((e,t)=>((0,o.wg)(),(0,o.j4)(w,{key:e.id,once:"",class:"preview-item"},{default:(0,o.w5)((()=>[(0,o.Wm)(h,{class:"q-ma-sm",onClick:e=>g.openPic(t)},{default:(0,o.w5)((()=>["video"!=e.media_type?((0,o.wg)(),(0,o.iD)("div",a,[(0,o.Wm)(p,{src:g.getImageDetail(t),loading:"eager","no-transition":"","no-spinner":"",ratio:1,class:"rounded-borders"},null,8,["src"])])):((0,o.wg)(),(0,o.iD)("div",d,[s,(0,o._)("div",r,[(0,o._)("video",{style:{width:"100%",height:"100%","object-fit":"cover","object-position":"50% 50%"},autoplay:"",loop:"",muted:"",playsinline:"",src:g.getImageDetail(t),class:"rounded-borders"},null,8,c)])]))])),_:2},1032,["onClick"])])),_:2},1024)))),128))])),(0,o.Wm)(_,{"transition-show":"jump-up","transition-hide":"jump-down",modelValue:l.showImageDetail,"onUpdate:modelValue":t[1]||(t[1]=e=>l.showImageDetail=e),maximized:""},{default:(0,o.w5)((()=>[(0,o.Wm)(y,{onCloseEvent:t[0]||(t[0]=e=>l.showImageDetail=!1),itemRepository:this.mediacollectionStore.collection,indexSelected:l.indexSelected,class:"full-height"},null,8,["itemRepository","indexSelected"])])),_:1},8,["modelValue"])])),_:1})}var g=i(67575),p=i(96694),h=i(33630),w=i(60499),y=i(68800);const _={components:{GalleryImageDetail:y.Z},setup(){const e=(0,g.h)(),t=(0,p.R)(),i=(0,h.r)();return{store:e,uiSettingsStore:t,mediacollectionStore:i,GalleryImageDetail:y.Z,indexSelected:(0,w.iH)(null),showImageDetail:(0,w.iH)(!1)}},computed:{itemId(){return this.$route.params.id},isGalleryEmpty(){return 0==this.mediacollectionStore.collection_number_of_items}},mounted(){},watch:{itemId(e,t){const i=this.mediacollectionStore.getIndexOfItemId(e);-1==i?console.error(`image id not found ${e}`):this.openPic(i)}},methods:{getImageDetail(e,t="thumbnail"){return this.mediacollectionStore.collection[e][t]},openPic(e){this.indexSelected=e,this.showImageDetail=!0}}};var I=i(11639),D=i(69885),S=i(21517),v=i(44458),f=i(70335),b=i(32074),k=i(69984),Z=i.n(k);const j=(0,I.Z)(_,[["render",u],["__scopeId","data-v-398add10"]]),q=j;Z()(_,"components",{QPage:D.Z,QIntersection:S.Z,QCard:v.Z,QImg:f.Z,QDialog:b.Z})}}]);