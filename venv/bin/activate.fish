# This file must be used with ". bin/activate.fish" *from fish* (http://fishshell.org)
# you cannot run it directly

function deactivate  -d "Exit virtualenv and return to normal shell environment"
    # reset old environment variables
    if test -n "$_OLD_VIRTUAL_PATH"
        set -gx PATH $_OLD_VIRTUAL_PATH
        set -e _OLD_VIRTUAL_PATH
    end
    if test -n "$_OLD_VIRTUAL_PYTHONHOME"
        set -gx PYTHONHOME $_OLD_VIRTUAL_PYTHONHOME
        set -e _OLD_VIRTUAL_PYTHONHOME
    end

    if test -n "$_OLD_FISH_PROMPT_OVERRIDE"
        functions -e fish_prompt
        set -e _OLD_FISH_PROMPT_OVERRIDE
        functions -c _old_fish_prompt fish_prompt
        functions -e _old_fish_prompt
    end

    set -e VIRTUAL_ENV
    if test "$argv[1]" != "nondestructive"
        # Self destruct!
        functions -e deactivate
    end
end

# unset irrelevant variables
deactivate nondestructive

set -gx VIRTUAL_ENV "/Users/collin/crmrepo/crmproject/venv"

set -gx _OLD_VIRTUAL_PATH $PATH
set -gx PATH "$VIRTUAL_ENV/bin" $PATH

# unset PYTHONHOME if set
if set -q PYTHONHOME
    set -gx _OLD_VIRTUAL_PYTHONHOME $PYTHONHOME
    set -e PYTHONHOME
end

if test -z "$VIRTUAL_ENV_DISABLE_PROMPT"
    # fish uses a function instead of an env var to generate the prompt.

    # save the current fish_prompt function as the function _old_fish_prompt
    functions -c fish_prompt _old_fish_prompt

    # with the original prompt function renamed, we can override with our own.
    function fish_prompt
        # Save the return status of the last command
        set -l old_status $status

        # Prompt override?
        if test -n "(venv) "
            printf "%s%s" "(venv) " (set_color normal)
        else
            # ...Otherwise, prepend env
            set -l _checkbase (basename "$VIRTUAL_ENV")
            if test $_checkbase = "__"
                # special case for Aspen magic directories
                # see http://www.zetadev.com/software/aspen/
                printf "%s[%s]%s " (set_color -b blue white) (basename (dirname "$VIRTUAL_ENV")) (set_color normal)
            else
                printf "%s(%s)%s" (set_color -b blue white) (basename "$VIRTUAL_ENV") (set_color normal)
            end
        end

        # Restore the return status of the previous command.
        echo "exit $old_status" | .
        _old_fish_prompt
    end

    set -gx _OLD_FISH_PROMPT_OVERRIDE "$VIRTUAL_ENV"
end

# disable nodeenv's prompt
# (prompt already changed by original virtualenv's script)
# https://github.com/ekalinin/nodeenv/issues/26
set NODE_VIRTUAL_ENV_DISABLE_PROMPT 1


# This file must be used with "source bin/activate.fish" *from fish*
# you cannot run it directly

function deactivate_node -d 'Exit nodeenv and return to normal environment.'
    # reset old environment variables
    if test -n "$_OLD_NODE_VIRTUAL_PATH"
        set -gx PATH $_OLD_NODE_VIRTUAL_PATH
        set -e _OLD_NODE_VIRTUAL_PATH
    end

    if test -n "$_OLD_NODE_PATH"
        set -gx NODE_PATH $_OLD_NODE_PATH
        set -e _OLD_NODE_PATH
    else
        set -e NODE_PATH
    end

    if test -n "$_OLD_NPM_CONFIG_PREFIX"
        set -gx NPM_CONFIG_PREFIX $_OLD_NPM_CONFIG_PREFIX
        set -e _OLD_NPM_CONFIG_PREFIX
    else
        set -e NPM_CONFIG_PREFIX
    end

    if test -n "$_OLD_npm_config_prefix"
        set -gx npm_config_prefix $_OLD_npm_config_prefix
        set -e _OLD_npm_config_prefix
    else
        set -e npm_config_prefix
    end

    if test -n "$_OLD_NODE_FISH_PROMPT_OVERRIDE"
        # Set an empty local `$fish_function_path` to allow the removal of
        # `fish_prompt` using `functions -e`.
        set -l fish_function_path

        # Erase virtualenv's `fish_prompt` and restore the original.
        functions -e fish_prompt
        functions -c _old_fish_prompt fish_prompt
        functions -e _old_fish_prompt
        set -e _OLD_NODE_FISH_PROMPT_OVERRIDE
    end

    if test (count $argv) = 0 -o "$argv[1]" != "nondestructive"
        # Self destruct!
        functions -e deactivate_node
    end
end

function freeze -d 'Show a list of installed packages - like `pip freeze`'
    set -l NPM_VER (npm -v | cut -d '.' -f 1)
    set -l RE "[a-zA-Z0-9\.\-]+@[0-9]+\.[0-9]+\.[0-9]+([\+\-][a-zA-Z0-9\.\-]+)*"

    if test "$NPM_VER" = "0"
        set -g NPM_LIST (npm list installed active >/dev/null ^/dev/null |                          cut -d ' ' -f 1 | grep -v npm)
    else
        set -l NPM_LS "npm ls -g"
        if test (count $argv) -gt 0 -a "$argv[1]" = "-l"
            set NPM_LS "npm ls"
            set -e argv[1]
        end
        set -l NPM_LIST (eval $NPM_LS | grep -E '^.{4}\w{1}' |                                         grep -o -E "$re" |                                         grep -v npm)
    end

    if test (count $argv) = 0
        echo $NPM_LIST
    else
        echo $NPM_LIST > $argv[1]
    end
end

# unset irrelevant variables
deactivate_node nondestructive

# NODE_VIRTUAL_ENV is the parent of the directory where this script is
set -gx NODE_VIRTUAL_ENV /Users/collin/crmrepo/crmproject/venv

set -gx _OLD_NODE_VIRTUAL_PATH $PATH
# The node_modules/.bin path doesn't exists and it will print a warning, and
# that's why we redirect stderr to /dev/null :)
set -gx PATH "$NODE_VIRTUAL_ENV/lib/node_modules/.bin" "$NODE_VIRTUAL_ENV/bin" $PATH ^/dev/null

if set -q NODE_PATH
    set -gx _OLD_NODE_PATH $NODE_PATH
    set -gx NODE_PATH "$NODE_VIRTUAL_ENV/lib/node_modules" $NODE_PATH
else
    set -gx NODE_PATH "$NODE_VIRTUAL_ENV/lib/node_modules"
end

if set -q NPM_CONFIG_PREFIX
    set -gx _OLD_NPM_CONFIG_PREFIX $NPM_CONFIG_PREFIX
end
set -gx NPM_CONFIG_PREFIX "$NODE_VIRTUAL_ENV"

if set -q npm_config_prefix
    set -gx _OLD_npm_config_prefix $npm_config_prefix
end
set -gx npm_config_prefix "$NODE_VIRTUAL_ENV"

if test -z "$NODE_VIRTUAL_ENV_DISABLE_PROMPT"
    # Copy the current `fish_prompt` function as `_old_fish_prompt`.
    functions -c fish_prompt _old_fish_prompt

    function fish_prompt
        # Save the current $status, for fish_prompts that display it.
        set -l old_status $status

        # Prompt override provided?
        # If not, just prepend the environment name.
        if test -n ""
            printf '%s%s' "" (set_color normal)
        else
            printf '%s(%s) ' (set_color normal) (basename "$NODE_VIRTUAL_ENV")
        end

        # Restore the original $status
        echo "exit $old_status" | source
        _old_fish_prompt
    end

    set -gx _OLD_NODE_FISH_PROMPT_OVERRIDE "$NODE_VIRTUAL_ENV"
end

set -e NODE_VIRTUAL_ENV_DISABLE_PROMPT
