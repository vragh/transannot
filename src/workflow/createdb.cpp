#include "Parameters.h"
#include "Debug.h"
#include "Util.h"
#include "FileUtil.h"
#include "CommandCaller.h"
//#include "createdb.sh.h"
#include "LocalParameters.h"

int createdb(int argc, const char **argv, const Command& command) {
    LocalParameters &par = LocalParameters::getLocalInstance();

    CommandCaller cmd
    cmd.addVariable("REMOVE_TMP", par.removeTmpFiles ? "TRUE" : NULL);

    return EXIT_SUCCESS;
}