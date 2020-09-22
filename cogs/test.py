   @commands.command(name='pause', aliases = ['pa', 'pau'])
    @commands.has_permissions()
    async def _pause(self, ctx: commands.Context):
        """Приостанавливает воспроизводимую в данный момент песню."""

        if not ctx.voice_state.is_playing and ctx.voice_state.voice.is_playing():
            ctx.voice_state.voice.pause()
            await ctx.message.add_reaction("⏯")

    @commands.command(name='resume', aliases=['r', 'res'])
    @commands.has_permissions()
    async def _resume(self, ctx: commands.Context):
        """Возобновляет приостановленную в данный момент песню."""

        if not ctx.voice_state.is_playing and ctx.voice_state.voice.is_paused():
            ctx.voice_state.voice.resume()
            await ctx.message.add_reaction("⏯")

    @commands.command(name='stop", aliases = ["s", "st"])
    @commands.has_permissions()
    async def _stop(self, ctx: commands.Context):
        """Останавливает воспроизведение песни и очищает очередь."""

        ctx.voice_state.songs.clear()

        if not ctx.voice_state.is_playing:
            ctx.voice_state.voice.stop()
            await ctx.message.add_reaction("⏹")
