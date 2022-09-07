import PySimpleGUI as sg
import download

sg.theme("DarkGrey12")

def tela_principal():
    layout = [
        [sg.Text("YOUTUBE DOWNLOAD")],
        [sg.Button("Baixar Músicas"),sg.Button("Baixar Vídeos")]
    ]
    return sg.Window("Youtube Download",layout,finalize=True)

def tela_musica():
    layout = [
        [sg.Text("Música Download")],
        [sg.Text("Link do vídeo:"),sg.InputText("",key="link_video")],
        [sg.Text("Diretorio da Pasta",key="text_diretorio"),sg.FolderBrowse(key="diretorio")],
        [sg.Button("Baixar Música"),sg.Button("Voltar")]
    ]
    return sg.Window("Música Download",layout,finalize=True)
    
def tela_video():
    layout = [
        [sg.Text("Vídeo Download")],
        [sg.Text("Link do vídeo:"),sg.InputText("",key="link_video1")],
        [sg.Text("Diretorio da Pasta",key="text_diretorio1"),sg.FolderBrowse(key="diretorio1")],
        [sg.Button("Baixar Vídeo"),sg.Button("Voltar")]
    ]
    return sg.Window("Vídeo Download",layout,finalize=True)

janela_principal = tela_principal()
janela_musica = None
janela_video = None

while True:
    janelas,eventos,valores = sg.read_all_windows()
    if eventos == sg.WINDOW_CLOSED:
        break

    if janelas == janela_principal and eventos == "Baixar Músicas":
        janela_principal.hide()
        janela_musica = tela_musica()

    if janelas == janela_musica and eventos == "Voltar":
        janela_musica.hide()
        janela_principal.un_hide()

    if janelas == janela_principal and eventos == "Baixar Vídeos":
        janela_principal.hide()
        janela_video = tela_video()

    if janelas == janela_video and eventos == "Voltar":
        janela_video.hide()
        janela_principal.un_hide()

    if janelas == janela_musica and eventos == "Baixar Música" and valores["diretorio"] == "":
        sg.Popup("Por Favor informe o local onde o arquivo vai ser salvo")
    
    if janelas == janela_musica and eventos == "Baixar Música" and valores["diretorio"] != "":
        link_video = valores["link_video"]
        pasta_arquivo = valores["diretorio"]
        sg.Popup("Vai aparecer que o youtube download não está respondendo. Isso é porque o download está sendo feito.Por favor click em OK e espere aparecer um Popup dizendo que o download está concluido")
        download.download_musica(link_video,pasta_arquivo)
        sg.Popup("Download Concluido")
        janela_musica["text_diretorio"].update("Por Favor informe o diretorio novamente")

    if janelas == janela_video and eventos == "Baixar Vídeo" and valores["diretorio1"] == "":
        sg.Popup("Por Favor informe o local onde o arquivo vai ser salvo")

    if janelas == janela_video and eventos == "Baixar Vídeo" and valores["diretorio1"] != "":
        link_video = valores["link_video1"]
        pasta_arquivo = valores["diretorio1"]
        sg.Popup("Vai aparecer que o youtube download não está respondendo. Isso é porque o download está sendo feito.Por favor click em OK e espere aparecer um Popup dizendo que o download está concluido")
        download.download_video(link_video,pasta_arquivo)
        sg.Popup("Download Concluido")
        janela_video["text_diretorio1"].update("Por Favor informe o diretorio novamente")




    
        