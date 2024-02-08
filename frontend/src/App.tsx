import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom"

import Login from './components/Login'
import Register from './components/Register'
import Home from './components/Home'
import PageNotFound from './components/PageNotFound'


function App() {
  return (
    <div>
      <Router>
            <Routes>
                <Route path='/login' element={<Login />} />
                <Route path='/register' element={<Register />} />
                <Route path='' element={<Home />} />
                <Route path='/404_page_not_found/' element={<PageNotFound />} />
            </Routes>
        </Router>
    </div>
  )
}

export default App
