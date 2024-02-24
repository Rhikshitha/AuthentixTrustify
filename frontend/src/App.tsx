import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom"

// import Login from './components/Login'
// import Register from './components/Register'
// import HomePage from './components/HomePage'
import PageNotFound from './components/PageNotFound'
import UserLogin from "./components/UserLogin"
import UserRegister from "./components/UserRegister"
import './App.css'
import HomePage from "./components/HomePage"



function App() {
  return (
    <div>
      <Router>
            <Routes>
                <Route path='/login' element={<UserLogin />} />
                <Route path='/register' element={<UserRegister />} />
                <Route path='' element={<HomePage />} />
                <Route path='/404_page_not_found/' element={<PageNotFound />} />
            </Routes>
        </Router>
    </div>
  )
}

export default App
