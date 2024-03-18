'use client';
import Image from "next/image";
import imgItem from '/public/next.svg'
import { useState } from "react";

export default function List() {
    let article = ['Tomatoes', 'Pasta', 'Coconut'];
    let [ea, setEa] = useState(0); // state 쓰면 html도 자동 재렌더링 해줌 
    return (
        <div>
            <h4 className="title">게시글 목록</h4>
            { 
                article.map((title, i)=> {
                    return (
                        <div className="article" key={i}>
                            {/* image 최적화 : lazy loading, 사이즈 최적화, layout shift * 최적화는 다 만들고나서 하는게 좋음*/}
                            {/* 외부 이미지 쓰려면 width height 지정해줘야하고 next.config.js 에 셋팅도 필요함 */}
                            <Image src={imgItem} alt={title} className="article-img" />  
                            <h4>{title}</h4>
                            <span> {ea} </span>
                            <button onClick={()=> {
                                setEa(ea + 1);
                            }}> + </button>
                        </div>
                    )
                })
            }
        </div>
    );
}