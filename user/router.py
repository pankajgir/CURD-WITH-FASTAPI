from fastapi import APIRouter,status,Form,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,RedirectResponse

router=APIRouter()

tamplates=Jinja2Templates(directory='user/tampletes')

@router.get('/',response_class=HTMLResponse)
async def user(request:Request):
    return tamplates.TemplateResponse('index.html',{'request':request})