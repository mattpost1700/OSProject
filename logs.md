   on
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.SetLocationCommand

PS C:\WINDOWS\system32> cd C:\Users\mattp\Desktop\WinProject
PS C:\Users\mattp\Desktop\WinProject> ls
PS C:\Users\mattp\Desktop\WinProject> $oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
PS C:\Users\mattp\Desktop\WinProject> if ($oldPath.Split(';') -inotcontains 'C:\minikube'){ `
>>   [Environment]::SetEnvironmentVariable('Path', $('{0};C:\minikube' -f $oldPath), [EnvironmentVariableTarget]::Machine) `
>> }
PS C:\Users\mattp\Desktop\WinProject> minikube start
minikube : The term 'minikube' is not recognized as the name of a cmdlet, function, script file, or operable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ minikube start
+ ~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (minikube:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\mattp\Desktop\WinProject> winget install minikube
The `msstore` source requires that you view the following agreements before using.
Terms of Transaction: https://aka.ms/microsoft-store-terms-of-transaction
The source requires the current machine's 2-letter geographic region to be sent to the backend service to function properly (ex. "US").

Do you agree to all the source agreements terms?
[Y] Yes  [N] No:
[Y] Yes  [N] No: T
[Y] Yes  [N] No: Y
Found Kubernetes - Minikube - A Local Kubernetes Development Environment [Kubernetes.minikube] Version 1.29.0
This application is licensed to you by its owner.
Microsoft is not responsible for, nor does it grant any licenses to, third-party packages.
Downloading https://github.com/kubernetes/minikube/releases/download/v1.29.0/minikube-installer.exe
  ██████████████████████████████  33.6 MB / 33.6 MB
Successfully verified installer hash
Starting package install...
Successfully installed
PS C:\Users\mattp\Desktop\WinProject> minikube start
minikube : The term 'minikube' is not recognized as the name of a cmdlet, function, script file, or operable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ minikube start
+ ~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (minikube:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\mattp\Desktop\WinProject> exec
exec : The term 'exec' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ exec
+ ~~~~
    + CategoryInfo          : ObjectNotFound: (exec:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\mattp\Desktop\WinProject> minikube start
minikube : The term 'minikube' is not recognized as the name of a cmdlet, function, script file, or operable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ minikube start
+ ~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (minikube:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\mattp\Desktop\WinProject> find minikube
FIND: Parameter format not correct
PS C:\Users\mattp\Desktop\WinProject> choco install minikube
choco : The term 'choco' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ choco install minikube
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (choco:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\mattp\Desktop\WinProject> winget install minikube
Found an existing package already installed. Trying to upgrade the installed package...
No applicable upgrade found.
PS C:\Users\mattp\Desktop\WinProject>
PS C:\Users\mattp\Desktop\WinProject> where winget
PS C:\Users\mattp\Desktop\WinProject> where winget
PS C:\Users\mattp\Desktop\WinProject> find winget
FIND: Parameter format not correct
PS C:\Users\mattp\Desktop\WinProject> where minikube
PS C:\Users\mattp\Desktop\WinProject> winget info
Windows Package Manager v1.4.10173
Copyright (c) Microsoft Corporation. All rights reserved.

Unrecognized command: 'info'

The winget command line utility enables installing applications and other packages from the command line.

usage: winget  [<command>] [<options>]

The following commands are available:
  install    Installs the given package
  show       Shows information about a package
  source     Manage sources of packages
  search     Find and show basic info of packages
  list       Display installed packages
  upgrade    Shows and performs available upgrades
  uninstall  Uninstalls the given package
  hash       Helper to hash installer files
  validate   Validates a manifest file
  settings   Open settings or set administrator settings
  features   Shows the status of experimental features                                                                    export     Exports a list of the installed packages                                                                     import     Installs all the packages in a file                                                                                                                                                                                                For more details on a specific command, pass it the help argument. [-?]                                                                                                                                                                         The following options are available:
  -v,--version              Display the version of the tool
  --info                    Display general info of the tool
  -?,--help                 Shows help about the selected command
  --wait                    Prompts the user to press any key before exiting
  --verbose,--verbose-logs  Enables verbose logging for WinGet
  --disable-interactivity   Disable interactive prompts

More help can be found at: https://aka.ms/winget-command-help
PS C:\Users\mattp\Desktop\WinProject> Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
Forcing web requests to allow TLS v1.2 (Required for requests to Chocolatey.org)
Getting latest version of the Chocolatey package for download.
Not using proxy.
Getting Chocolatey from https://community.chocolatey.org/api/v2/package/chocolatey/1.3.0.
Downloading https://community.chocolatey.org/api/v2/package/chocolatey/1.3.0 to C:\Users\mattp\AppData\Local\Temp\chocolatey\chocoInstall\chocolatey.zip
Not using proxy.
Extracting C:\Users\mattp\AppData\Local\Temp\chocolatey\chocoInstall\chocolatey.zip to C:\Users\mattp\AppData\Local\Temp\chocolatey\chocoInstall
Installing Chocolatey on the local machine
Creating ChocolateyInstall as an environment variable (targeting 'Machine')
  Setting ChocolateyInstall to 'C:\ProgramData\chocolatey'
WARNING: It's very likely you will need to close and reopen your shell
  before you can use choco.
Restricting write permissions to Administrators
We are setting up the Chocolatey package repository.
The packages themselves go to 'C:\ProgramData\chocolatey\lib'
  (i.e. C:\ProgramData\chocolatey\lib\yourPackageName).
A shim file for the command line goes to 'C:\ProgramData\chocolatey\bin'
  and points to an executable in 'C:\ProgramData\chocolatey\lib\yourPackageName'.

Creating Chocolatey folders if they do not already exist.

WARNING: You can safely ignore errors related to missing log files when
  upgrading from a version of Chocolatey less than 0.9.9.
  'Batch file could not be found' is also safe to ignore.
  'The system cannot find the file specified' - also safe.
chocolatey.nupkg file not installed in lib.
 Attempting to locate it from bootstrapper.
PATH environment variable does not have C:\ProgramData\chocolatey\bin in it. Adding...
WARNING: Not setting tab completion: Profile file does not exist at
'C:\Users\mattp\OneDrive\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1'.
Chocolatey (choco.exe) is now ready.
You can call choco from anywhere, command line or powershell by typing choco.
Run choco /? for a list of functions.
You may need to shut down and restart powershell and/or consoles
 first prior to using choco.
Ensuring Chocolatey commands are on the path
Ensuring chocolatey.nupkg is in the lib folder
PS C:\Users\mattp\Desktop\WinProject> choco
Chocolatey v1.3.0
Please run 'choco -?' or 'choco <command> -?' for help menu.
PS C:\Users\mattp\Desktop\WinProject> choco install
Chocolatey v1.3.0
Package name is required. Please pass at least one package name to install.
PS C:\Users\mattp\Desktop\WinProject> ^C
PS C:\Users\mattp\Desktop\WinProject> choco install minikube
Chocolatey v1.3.0
Installing the following packages:
minikube
By installing, you accept licenses for the packages.
Progress: Downloading kubernetes-cli 1.26.2... 100%
Progress: Downloading Minikube 1.29.0... 100%

kubernetes-cli v1.26.2 [Approved]
kubernetes-cli package files install completed. Performing other installation steps.
The package kubernetes-cli wants to run 'chocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[A]ll - yes to all/[N]o/[P]rint): Y

Extracting 64-bit C:\ProgramData\chocolatey\lib\kubernetes-cli\tools\kubernetes-client-windows-amd64.tar.gz to C:\ProgramData\chocolatey\lib\kubernetes-cli\tools...
C:\ProgramData\chocolatey\lib\kubernetes-cli\tools
Extracting 64-bit C:\ProgramData\chocolatey\lib\kubernetes-cli\tools\kubernetes-client-windows-amd64.tar to C:\ProgramData\chocolatey\lib\kubernetes-cli\tools...
C:\ProgramData\chocolatey\lib\kubernetes-cli\tools
 ShimGen has successfully created a shim for kubectl-convert.exe
 ShimGen has successfully created a shim for kubectl.exe
 The install of kubernetes-cli was successful.
  Software installed to 'C:\ProgramData\chocolatey\lib\kubernetes-cli\tools'

Minikube v1.29.0 [Approved]
minikube package files install completed. Performing other installation steps.
 ShimGen has successfully created a shim for minikube.exe
 The install of minikube was successful.
  Software installed to 'C:\ProgramData\chocolatey\lib\Minikube'

Chocolatey installed 2/2 packages.
 See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).
PS C:\Users\mattp\Desktop\WinProject> minikube
minikube provisions and manages local Kubernetes clusters optimized for development workflows.

Basic Commands:
  start            Starts a local Kubernetes cluster
  status           Gets the status of a local Kubernetes cluster
  stop             Stops a running local Kubernetes cluster
  delete           Deletes a local Kubernetes cluster
  dashboard        Access the Kubernetes dashboard running within the minikube cluster
  pause            pause Kubernetes
  unpause          unpause Kubernetes

Images Commands:
  docker-env       Provides instructions to point your terminal's docker-cli to the Docker Engine inside minikube.
(Useful for building docker images directly inside minikube)
  podman-env       Configure environment to use minikube's Podman service
  cache            Manage cache for images
  image            Manage images

Configuration and Management Commands:
  addons           Enable or disable a minikube addon
  config           Modify persistent configuration values
  profile          Get or list the current profiles (clusters)
  update-context   Update kubeconfig in case of an IP or port change

Networking and Connectivity Commands:
  service          Returns a URL to connect to a service
  tunnel           Connect to LoadBalancer services

Advanced Commands:
  mount            Mounts the specified directory into minikube
  ssh              Log into the minikube environment (for debugging)
  kubectl          Run a kubectl binary matching the cluster version
  node             Add, remove, or list additional nodes
  cp               Copy the specified file into minikube

Troubleshooting Commands:
  ssh-key          Retrieve the ssh identity key path of the specified node
  ssh-host         Retrieve the ssh host key of the specified node
  ip               Retrieves the IP address of the specified node
  logs             Returns logs to debug a local Kubernetes cluster
  update-check     Print current and latest version number
  version          Print the version of minikube
  options          Show a list of global command-line options (applies to all commands).

Other Commands:
  completion       Generate command completion for a shell
  license          Outputs the licenses of dependencies to a directory

Use "minikube <command> --help" for more information about a given command.
PS C:\Users\mattp\Desktop\WinProject> minikube start
* minikube v1.29.0 on Microsoft Windows 11 Home 10.0.22000.1574 Build 22000.1574
* Automatically selected the virtualbox driver
* Downloading VM boot image ...
    > minikube-v1.29.0-amd64.iso....:  65 B / 65 B [---------] 100.00% ? p/s 0s
    > minikube-v1.29.0-amd64.iso:  276.35 MiB / 276.35 MiB  100.00% 49.96 MiB p
* Starting control plane node minikube in cluster minikube
* Downloading Kubernetes v1.26.1 preload ...
    > preloaded-images-k8s-v18-v1...:  397.05 MiB / 397.05 MiB  100.00% 52.98 M
* Creating virtualbox VM (CPUs=2, Memory=4000MB, Disk=20000MB) ...
! This VM is having trouble accessing https://registry.k8s.io
* To pull new external images, you may need to configure a proxy: https://minikube.sigs.k8s.io/docs/reference/networking/proxy/

X Exiting due to RUNTIME_ENABLE: sudo systemctl restart docker: Process exited with status 1
stdout:

stderr:
Job for docker.service failed because the control process exited with error code.
See "systemctl status docker.service" and "journalctl -xe" for details.

*
╭─────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                             │
│    * If the above advice does not help, please let us know:                                 │
│      https://github.com/kubernetes/minikube/issues/new/choose                               │
│                                                                                             │
│    * Please run `minikube logs --file=logs.txt` and attach logs.txt to the GitHub issue.    │
│                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────╯

PS C:\Users\mattp\Desktop\WinProject>
PS C:\Users\mattp\Desktop\WinProject>
PS C:\Users\mattp\Desktop\WinProject>
PS C:\Users\mattp\Desktop\WinProject> docker ps
docker : The term 'docker' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path
is correct and try again.
At line:1 char:1
+ docker ps
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (docker:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\mattp\Desktop\WinProject> choco install docker
Chocolatey v1.3.0
Installing the following packages:
docker
By installing, you accept licenses for the packages.
Progress: Downloading docker-cli 23.0.1... 100%
Progress: Downloading docker 99.0.0... 100%

docker-cli v23.0.1 [Approved]
docker-cli package files install completed. Performing other installation steps.
 ShimGen has successfully created a shim for docker.exe
 The install of docker-cli was successful.
  Software installed to 'C:\ProgramData\chocolatey\lib\docker-cli'

docker v99.0.0 [Approved]
docker package files install completed. Performing other installation steps.
The package docker wants to run 'chocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[A]ll - yes to all/[N]o/[P]rint): Y

WARNING: This package is superseeded by docker-cli, you should install that package from now on.
 The install of docker was successful.
  Software install location not explicitly set, it could be in package or
  default install location of installer.

Chocolatey installed 2/2 packages.
 See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).
PS C:\Users\mattp\Desktop\WinProject> choco feature enable -n allowGlobalConfirmation
Chocolatey v1.3.0
Enabled allowGlobalConfirmation
PS C:\Users\mattp\Desktop\WinProject> export NO_PROXY=localhost,127.0.0.1,10.96.0.0/12,192.168.59.0/24,192.168.49.0/24,192.168.39.0/24
export : The term 'export' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path
is correct and try again.
At line:1 char:1
+ export NO_PROXY=localhost,127.0.0.1,10.96.0.0/12,192.168.59.0/24,192. ...
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (export:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\mattp\Desktop\WinProject> set NO_PROXY=localhost,127.0.0.1,10.96.0.0/12,192.168.59.0/24,192.168.49.0/24,192.168.39.0/24
PS C:\Users\mattp\Desktop\WinProject> minikube startr
Error: unknown command "startr" for "minikube"

Did you mean this?
        start

Run 'minikube --help' for usage.
PS C:\Users\mattp\Desktop\WinProject> minikube start
* minikube v1.29.0 on Microsoft Windows 11 Home 10.0.22000.1574 Build 22000.1574
* Using the virtualbox driver based on existing profile
* Starting control plane node minikube in cluster minikube
* Updating the running virtualbox "minikube" VM ...
* Preparing Kubernetes v1.26.1 on Docker 20.10.23 ...
  - Generating certificates and keys ...
  - Booting up control plane ...
  - Configuring RBAC rules ...
* Configuring bridge CNI (Container Networking Interface) ...
  - Using image gcr.io/k8s-minikube/storage-provisioner:v5
* Verifying Kubernetes components...
* Enabled addons: storage-provisioner, default-storageclass
* Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
PS C:\Users\mattp\Desktop\WinProject>
PS C:\Users\mattp\Desktop\WinProject> minikube info
Error: unknown command "info" for "minikube"
Run 'minikube --help' for usage.
PS C:\Users\mattp\Desktop\WinProject> minikube --info
Error: unknown flag: --info
See 'minikube --help' for usage.
PS C:\Users\mattp\Desktop\WinProject> minikube --ehlp
Error: unknown flag: --ehlp
See 'minikube --help' for usage.
PS C:\Users\mattp\Desktop\WinProject> minikube --help
minikube provisions and manages local Kubernetes clusters optimized for development workflows.

Basic Commands:
  start            Starts a local Kubernetes cluster
  status           Gets the status of a local Kubernetes cluster
  stop             Stops a running local Kubernetes cluster
  delete           Deletes a local Kubernetes cluster
  dashboard        Access the Kubernetes dashboard running within the minikube cluster
  pause            pause Kubernetes
  unpause          unpause Kubernetes

Images Commands:
  docker-env       Provides instructions to point your terminal's docker-cli to the Docker Engine inside minikube.
(Useful for building docker images directly inside minikube)
  podman-env       Configure environment to use minikube's Podman service
  cache            Manage cache for images
  image            Manage images

Configuration and Management Commands:
  addons           Enable or disable a minikube addon
  config           Modify persistent configuration values
  profile          Get or list the current profiles (clusters)
  update-context   Update kubeconfig in case of an IP or port change

Networking and Connectivity Commands:
  service          Returns a URL to connect to a service
  tunnel           Connect to LoadBalancer services

Advanced Commands:
  mount            Mounts the specified directory into minikube
  ssh              Log into the minikube environment (for debugging)
  kubectl          Run a kubectl binary matching the cluster version
  node             Add, remove, or list additional nodes
  cp               Copy the specified file into minikube

Troubleshooting Commands:
  ssh-key          Retrieve the ssh identity key path of the specified node
  ssh-host         Retrieve the ssh host key of the specified node
  ip               Retrieves the IP address of the specified node
  logs             Returns logs to debug a local Kubernetes cluster
  update-check     Print current and latest version number
  version          Print the version of minikube
  options          Show a list of global command-line options (applies to all commands).

Other Commands:
  completion       Generate command completion for a shell
  license          Outputs the licenses of dependencies to a directory

Use "minikube <command> --help" for more information about a given command.
PS C:\Users\mattp\Desktop\WinProject> minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

PS C:\Users\mattp\Desktop\WinProject> minikube dashboard
* Enabling dashboard ...
  - Using image docker.io/kubernetesui/metrics-scraper:v1.0.8
  - Using image docker.io/kubernetesui/dashboard:v2.7.0
* Some dashboard features require the metrics-server addon. To enable all features please run:

        minikube addons enable metrics-server


* Verifying dashboard health ...
* Launching proxy ...
* Verifying proxy health ...
* Opening http://127.0.0.1:58405/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/ in your default browser...
PS C:\Users\mattp\Desktop\WinProject> minikube
minikube provisions and manages local Kubernetes clusters optimized for development workflows.

Basic Commands:
  start            Starts a local Kubernetes cluster
  status           Gets the status of a local Kubernetes cluster
  stop             Stops a running local Kubernetes cluster
  delete           Deletes a local Kubernetes cluster
  dashboard        Access the Kubernetes dashboard running within the minikube cluster
  pause            pause Kubernetes
  unpause          unpause Kubernetes

Images Commands:
  docker-env       Provides instructions to point your terminal's docker-cli to the Docker Engine inside minikube.
(Useful for building docker images directly inside minikube)
  podman-env       Configure environment to use minikube's Podman service
  cache            Manage cache for images
  image            Manage images

Configuration and Management Commands:
  addons           Enable or disable a minikube addon
  config           Modify persistent configuration values
  profile          Get or list the current profiles (clusters)
  update-context   Update kubeconfig in case of an IP or port change

Networking and Connectivity Commands:
  service          Returns a URL to connect to a service
  tunnel           Connect to LoadBalancer services

Advanced Commands:
  mount            Mounts the specified directory into minikube
  ssh              Log into the minikube environment (for debugging)
  kubectl          Run a kubectl binary matching the cluster version
  node             Add, remove, or list additional nodes
  cp               Copy the specified file into minikube

Troubleshooting Commands:
  ssh-key          Retrieve the ssh identity key path of the specified node
  ssh-host         Retrieve the ssh host key of the specified node
  ip               Retrieves the IP address of the specified node
  logs             Returns logs to debug a local Kubernetes cluster
  update-check     Print current and latest version number
  version          Print the version of minikube
  options          Show a list of global command-line options (applies to all commands).

Other Commands:
  completion       Generate command completion for a shell
  license          Outputs the licenses of dependencies to a directory

Use "minikube <command> --help" for more information about a given command.
PS C:\Users\mattp\Desktop\WinProject> kubectl get nodes
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   13m   v1.26.1
PS C:\Users\mattp\Desktop\WinProject> kubectl get pods
No resources found in default namespace.
PS C:\Users\mattp\Desktop\WinProject> kubectl get namespaces
NAME                   STATUS   AGE
default                Active   13m
kube-node-lease        Active   13m
kube-public            Active   13m
kube-system            Active   13m
kubernetes-dashboard   Active   6m25s
PS C:\Users\mattp\Desktop\WinProject>  minikube addons enable metrics-server
* metrics-server is an addon maintained by Kubernetes. For any concerns contact minikube on GitHub.
You can view the list of minikube maintainers at: https://github.com/kubernetes/minikube/blob/master/OWNERS
  - Using image registry.k8s.io/metrics-server/metrics-server:v0.6.2
* The 'metrics-server' addon is enabled
PS C:\Users\mattp\Desktop\WinProject> @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
At line:1 char:3
+ @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoPro ...
+   ~
No characters are allowed after a here-string header but before the end of the line.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : UnexpectedCharactersAfterHereStringHeader

PS C:\Users\mattp\Desktop\WinProject> kubectl get pods
No resources found in default namespace.
PS C:\Users\mattp\Desktop\WinProject> kubectl get namespaces
NAME                   STATUS   AGE
default                Active   13h
kube-node-lease        Active   13h
kube-public            Active   13h
kube-system            Active   13h
kubernetes-dashboard   Active   13h