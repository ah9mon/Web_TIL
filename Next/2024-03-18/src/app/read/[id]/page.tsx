export default function Read(props : any) {
    // return() 안에 HTML 넣을때 1개 <태그>로 시작해서 끝나야함
    return ( 
        <>
            <h2 className="title">Read</h2>
            <p className="article">게시글 :{props.params.id}</p>
        </>
        
    );
}