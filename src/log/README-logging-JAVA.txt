
# Logged
--------

package log;
import org.apache.log4j.Logger;

public interface Logged {
	static final Logger log = Logger.getLogger(Logged.class);
}


# LoggerConsole
---------------

package log;

import java.io.ByteArrayInputStream;

import org.apache.log4j.LogManager;


public class LoggerConsole implements Logged{

	private static String ROOT_LOGGER = 
		"log4j.rootLogger=DEBUG,STDOUT\r\n"
	+	"\r\n"
	;

//	private static String LOGGERS = 
//		"log4j.logger.test=DEBUG,STDOUT\r\n"
//	+	"log4j.additivity.test=false\r\n"
//	+	"\r\n"
//	;

	private static String APPENDERS =  
		"log4j.appender.STDOUT=org.apache.log4j.ConsoleAppender\r\n"
	+	"log4j.appender.STDOUT.layout=org.apache.log4j.PatternLayout\r\n"
	+	"log4j.appender.STDOUT.layout.ConversionPattern=%d %5p (%C:%L) - %m%n\r\n"
	+	"\r\n"
	;
	
//	private static String LOG4J_CONFIG = ROOT_LOGGER + LOGGERS  + APPENDERS;
	private static String LOG4J_CONFIG = ROOT_LOGGER  + APPENDERS;


	public static void initLoggers() {
		Log4jInit.initLogger(new ByteArrayInputStream(LOG4J_CONFIG.getBytes()));
	}
}


# Log4jInit
-----------

package log;

import java.io.InputStream;
import java.util.Properties;

import org.apache.log4j.Level;
import org.apache.log4j.PropertyConfigurator;

// TODO : ticket log + environnement global

public class Log4jInit implements Logged
{
	
	public static void initLogger(InputStream in) {
		try {
			Properties props = new Properties();
			props.load(in);
			PropertyConfigurator.configure(props);
		} catch (Exception e) {
			e.printStackTrace();
		}
		log.debug("logger on");
	}
}



# PropertiesFileSaverTest
-------------------------

public class PropertiesFileSaverTest {
	
	public static Logger log = Logger.getLogger(PropertiesFileSaverTest.class);
	

	@BeforeClass
	public static void initializeTest() {
        LoggerConsole.initLoggers();
	}
	

