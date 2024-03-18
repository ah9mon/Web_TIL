import data from './data';

export default function Cart() {
    return (
        <div>
            <h4 className="title">Cart</h4>
            {data.cart.map((itemName,i) => {
                return (
                <div>
                    <CartItem itemName = {itemName}/>
                </div>);
            })}
            <Button color = 'red'/>
            <Button color = 'blue'/>
        </div>
    );
}
// next에는 컴포넌트 2개 
// 1. server component
// js 기능 넣을 수 없음 onClick 같은거 
// js 기능 없어서 로딩 속도가 빠름 
// 큰페이지는 서버 컴포넌트가 많은게 좋음 

// 2. client component
// 'use client' 쓰면 client component 됨 
// 페이지 로드하는데 js 많이 필요 -> 로딩속도 느림 
// hydration 필요해서

// next에는 deduplication 있어서 데이터 가져올떄 반복해도 괜찮음

function CartItem(props : any) {
    return (
        <div className="cart-item">
            <p>{props.itemName}</p>
            <p>$30</p>
            <p>1개</p>
        </div>
    );
}

function Button(props : any) {
    return (
        <input type="button" value="buttttom" style={{background : `${props.color}`}}/>
    );
}