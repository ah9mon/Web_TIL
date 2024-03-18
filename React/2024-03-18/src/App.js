import { useState } from 'react';
import './App.css';

function Article(props) {
  return <article>
    <h2>{props.title}</h2>
    {props.body}
  </article>
}

function Nav(props) {
  const lis = []
  
  for(let i = 0; i < props.topics.length; i++) {
    let t = props.topics[i];
    lis.push(<li key={t.id}>
      <a id = {t.id} href={`/read/${t.id}`} onClick={(event) => {
        event.preventDefault();
        props.onChangeMode(Number(event.target.id)); // event.target = 이벤트를 유발시킨 태그 = a태크 // 태그의 속성이 되면 뮨자열이 됨 
      }}>{t.title}</a></li>)
  }
  
  return <nav>
    <ol>
      {lis}
    </ol>
  </nav>
}

function Header(props) {
  return <header>
    <h1><a href='/' onClick={(event)=>{
      event.preventDefault(); // a태크가 동작하는 기본동작을 방지 -> 클릭해도 reload 일어나지 않음
      props.onChangeMode();
    }}>{props.title}</a></h1>
  </header>
}

function Create(props) {
  return <article>
    <h2>Create</h2>
    <form onSubmit={event => {
      event.preventDefault();
      const title = event.target.title.value; // event target 이란 이벤트가 발생한 태그를 가리킴
      const body = event.target.body.value;
      props.onCreate(title, body);
    }}>
      <p><input type="text" name="title" placeholder="title"/></p>
      <p><textarea name="body" placeholder='body'></textarea></p>
      <p><input type="submit" value = "Create" /></p>
    </form>
  </article>
}

function Update(props) {
  const [title, setTitle] = useState(props.title);
  const [body, setBody] = useState(props.body);
  return <article>
    <h2>Update</h2>
    <form onSubmit={event => {
      event.preventDefault();
      const title = event.target.title.value; // event target 이란 이벤트가 발생한 태그를 가리킴
      const body = event.target.body.value;
      props.onUpdate(title, body);
    }}>
      <p><input type="text" name="title" placeholder="title" value={title} onChange={event=>{
        setTitle(event.target.value);
      }}/></p>
      <p><textarea name="body" placeholder='body' value = {body} onChange={event => {
        setBody(event.target.value);
      }}></textarea></p>
      <p><input type="submit" value = "Update" /></p>
    </form>
  </article>
}

function App() {
  // let _mode = useState('WELCOME'); // state의 초기값 
  // const mode = _mode[0]; // useState[0] 로 초기값 읽음
  // const setMode = _mode[1]; // useState[1] 로 변경함
  const [mode, setMode] = useState('WELCOME');
  const [id, setId] = useState(null);
  const [nextId, setNextId] = useState(4);
  const [topics,setTopics] = useState([
    {id : 1, title:'html', body:'html is ...'},
    {id : 2, title:'css', body:'css is ...'},
    {id : 3, title:'js', body:'JavaScript is ...'}
  ]);

  let content = null;
  let contextControl = null;
  if (mode === 'WELCOME') {
    content = <Article title = "Welcome" body = "Hello, WEB"></Article>
  } else if (mode === 'READ') {
    let title, body = null;
    for (let i = 0; i < topics.length; i++) {
      if (topics[i].id === (id)) {
        title = topics[i].title;
        body = topics[i].body;
        break;
      }
    }
    content = <Article title = {title} body = {body}></Article>
    contextControl = <>
    <li><a href={`/update/${id}`} onClick={event => {
      event.preventDefault();
      setMode('UPDATE');
    }}>Update</a></li>
    <li><input type="button" value = "Delete" onClick={() => {
      const newTopics = [];
      for (let i = 0; i < topics.length; i++) {
        if (topics[i].id !== id) {
          newTopics.push(topics[i]);
        }
      }
      setTopics(newTopics);
      setMode('WELCOME');
    }}/></li>
    </>
  } else if (mode === 'CREATE') {
    content = <Create onCreate={(_title, _body) => {
      const newTopic = {id:nextId, title:_title, body:_body};
      const newTopics = [...topics];
      newTopics.push(newTopic);
      setTopics(newTopics);
      setMode('READ');
      setId(nextId);
      setNextId(nextId + 1);
    }}></Create>
  } else if (mode === 'UPDATE') {
    let title, body = null;
    for (let i = 0; i < topics.length; i++) {
      if (topics[i].id === (id)) {
        title = topics[i].title;
        body = topics[i].body;
        break;
      }
    }
    content = <Update title = {title} body = {body} onUpdate={(_title, _body) => {
      const updatedTopic = {id:id,title:_title, body:_body};
      const newTopics = [...topics];
      for (let i = 0; i<newTopics.length;i++) {
        if (newTopics[i].id === id) {
          newTopics[i] = updatedTopic;
          break;
        }
      }
      setTopics(newTopics);
      setMode('READ');
    }}></Update>
  }
  return (
    <div>
      <Header title = "Main Page" onChangeMode={()=>{
        setMode('WELCOME');
      }}></Header>
      <Nav topics = {topics} onChangeMode={(_id)=>{
        setMode('READ');
        setId(_id);
      }}></Nav>
      {content}
      <ul>
      <li>
      <a href='/create' onClick={event => {
        event.preventDefault();
        setMode('CREATE');
      }}>Create</a>
      </li>
      {contextControl}
      </ul>
    </div>
  );
}

export default App;
