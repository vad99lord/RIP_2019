import React from 'react';
import './Home.css';
//import logo from '../../img/logo.svg'

// class Home extends React.Component {
// state = {
//     text:'Hello from state'
// };
//
// HandleTextClick=()=>
// {
//     this.setState({text:'Change State'})
//     console.log(this.props);
// };
//
//     render() {
//     return (
//         <div className="Home">
//           <header className="Home-header">
//             <div onClick={()=>(console.log(this.state.text)) }>
//               <img src={logo} className="Home-logo" alt="logo" />
//             </div>
//             <p onClick={this.HandleTextClick}>
//               Edit <code>src/Home.js</code> and save to reload.
//             </p>
//             <a
//                 className="Home-link"
//                 href="https://reactjs.org"
//                 target="_blank"
//                 rel="noopener noreferrer"
//             >
//               Learn React
//             </a>
//           </header>
//         </div>
//     );
//   }
//
// }

//export default Home;

export default ({list}) => (
    <div>
        {
            list.map(repo => (
                <li key={repo.id}>{repo.name}</li>
            ))
        }
    </div>
);