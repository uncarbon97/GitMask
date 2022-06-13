# 模板: commit-msg
TEMPLATE_COMMIT_MSG = '''#!/bin/sh

echo "-------- GitMask HOOK BEGIN --------"
exitCode=0
ret="$(gitmask --equals {} | grep "False")"
# echo $ret
if test "$ret" != ""; then
	gitmask --assign {}
	echo "GitMask assign finished. Please commit again."
	exitCode=1
fi
echo "-------- GitMask HOOK END --------"
exit $exitCode
'''