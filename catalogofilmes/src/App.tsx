
import { Button } from "./components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "./components/ui/card";
import { Search } from "lucide-react"
import { Input } from "./components/ui/input";

export function App() {
  

  return (
   <main className="h-screen flex w-full">

    <div className="bg-slate-600 w-full h-full flex">

      <section className="flex items-center justify-center h-screen w-screen flex-col">
        <Card>
          <CardHeader className="tx">
            <CardTitle className="text-4xl">
              Pesquise o seu Filme
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex items-center flex-row">
              <Input type="text" placeholder="Digite um filme" className="text-lg mr-4 w-96"></Input>
              
              <Button type="submit">
                <Search></Search>
                Pesquisar
              </Button>
            </div>
          </CardContent>
        </Card>
      </section>

    </div>
   </main>
  )
}


